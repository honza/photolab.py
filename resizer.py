import os
import Image

EXTENSIONS = ('.jpg', '.JPG', '.jpeg', '.JPEG',)

class Resizer(object):

    def __init__(self, source, destination, quality, extensions=None):
        self.source = source
        self.destination = destination
        self.quality = quality
        if not extensions:
            self.extensions = EXTENSIONS
        else:
            self.extensions = extensions
        self.cwd = os.getcwd()
        self.path = os.path.join(self.cwd, self.source)
        self.files = self._get_files()

    def _get_files(self):
        all_files = os.listdir(self.path)
        all_files.sort()
        return all_files

    def run(self):

        for a in self.files:
            if not a.endswith(self.extensions):
                continue
            print a
            name = os.path.join(self.path, a)
            img = Image.open(name)

            size = img.size
            w = size[0]
            h = size[1]

            if w > h:
                s = (800, 533)
            else:
                s = (533, 800)

            n = img.resize(s, Image.ANTIALIAS)
            new_name = os.path.join(self.cwd, '%s/%s' % (self.destination, a))
            n.save(new_name, quality=self.quality)
