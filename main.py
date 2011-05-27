"""
Photolap.py
"""
import os
import sys
from bottle import route, run, get, post
from bottle import jinja2_view as view
from bottle import static_file, request
from resizer import Resizer
from renamer import PyRenamer

# We need to know where the images are stored
if len(sys.argv) != 2:
    print "Please supply a path to your files."
    sys.exit(1)

path = sys.argv[1]

# Set up some user-specific globals
SOURCE = os.path.abspath(path)
THUMB_DIR = os.path.join(SOURCE, 'tmp')
if not os.path.exists(THUMB_DIR):
    os.mkdir(THUMB_DIR)
DONE_DIR = os.path.join(SOURCE, 'done')
if not os.path.exists(DONE_DIR):
    os.mkdir(DONE_DIR)

# Set up some globals for photolab itself
ROOT = os.path.abspath(os.path.dirname(__file__))
STATIC = os.path.join(ROOT, 'static')
EXTENSIONS = ('.jpg', '.JPG', '.jpeg', '.JPEG',)

def _copy_image(fn):
    """
    Copy an image from its source directory to the done directory
    """
    source = os.path.join(SOURCE, fn)
    dest = os.path.join(DONE_DIR, fn)
    os.system("cp %s %s" % (source, dest))


def _remove_junk(array):
    new = []
    for i in array:
        if i.endswith(EXTENSIONS):
            new.append(i)
    return new


@route('/')
@view('index')
def index():
    files = _remove_junk(os.listdir(SOURCE))
    return {
        'pictures': files
    }


@route('/static/:filename')
def server_static(filename):
    """
    Server application files (js, css)
    """
    return static_file(filename, root=STATIC)


@route('/media/:filename')
def media(filename):
    """
    Server user's media
    """
    return static_file(filename, root=THUMB_DIR)


@get('/process')
def ajax():
    """
    Create thumbnails for files in the source directory
    """
    try:
        r = Resizer(SOURCE, THUMB_DIR, 75)
        r.run()
    except Exception, e:
        print e
    return 'done!'


@get('/sort/')
@view('home')
def sort():
    """
    Present user with a screen where they can discard images
    """
    pictures = os.listdir(THUMB_DIR)
    return {
        'pictures': pictures,
        'process': True
    }


@post('/create-final')
def final():
    """
    Take all selected images and copy their originals into `done` and then
    rename them into something useful.
    """
    pictures = request.forms.get('pictures')
    place = request.forms.get('place')
    for p in pictures.split(','):
        _copy_image(p)
    try:
        r = PyRenamer(DONE_DIR, place)
        r.run()
    except Exception, e:
        print e
    return 'ok'


run(host='localhost', port=8000, reloader=True)
