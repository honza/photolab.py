import os
import sys
import Image # Python Imaging Library


class PyRenamer(object):

    def __init__(self, path, place):
        print path
        self.place = place
        self.path = path
        self.count = 0
        self.filenames = []
        self.dates = {} # key is a date, value is a number of files
        self._get_data()

    def _get_data(self):
        self.count = 0
        for originalfname in os.listdir(self.path):
            if originalfname.startswith('20') or originalfname.startswith('DSC'):
                self.count += 1
                self._process_file(originalfname)

    def _process_file(self, filename):
        filename = os.path.join(self.path, filename)
        i = Image.open(filename)
        d = i._getexif()[36867]
        s = d.split(" ")[0]
        dd = s.replace(':', '')
        if dd not in self.dates:
            self.dates[dd] = 1
        else:
            self.dates[dd] += 1
        t = (filename, dd, self.dates[dd],)
        self.filenames.append(t)

    def _get_num(self, file):
        count = self.dates[file[1]]
        if count < 10:
            return str(file[2])
        elif count < 100:
            if file[2] < 10:
                return '0' + str(file[2])
            else:
                return str(file[2])
        elif count < 1000:
            if file[2] < 10:
                return '00' + str(file[2])
            elif file[2] < 100:
                return '0' + str(file[2])
            else:
                return str(file[2])

    def run(self):
        for f in self.filenames:
            num = self._get_num(f)
            n = "%s_%s_%s.jpg" % (f[1], self.place, num,)
            n = os.path.join(self.path, n)
            os.rename(f[0], n)
    

if __name__ == '__main__':
    try:
        place = sys.argv[1]
    except IndexError:
        print 'No place specified'
        sys.exit(0)
    p = PyRenamer(place)
