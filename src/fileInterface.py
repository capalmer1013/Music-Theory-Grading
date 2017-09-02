"""
interface for musicxml files
"""
import music21
import glob


class File(object):
    def __init__(self, filename=None):
        if filename:
            self.open(filename)

        else:
            self.score = music21.stream.Stream()
            self.filename = ''

    def open(self, filename):
        if not(filename[-3:] != ".xml" or filename[-3:] != ".mxl"):
            self.filename = ''
            return "Not a valid filetype."

        self.filename = filename
        self.score = music21.converter.parse(filename).flat
        return self.filename


class FileDir(object):
    def __init__(self, dirname=None):
        if not dirname:
            self.listOfFiles = []
            self.dirname = None
        else:
            self.openDir(dirname)

    def openDir(self, dirname):
        self.dirname = dirname
        self.listOfFiles = [File(x) for x in glob.glob(dirname + '/*')]
        return '\n'.join([x.filename for x in self.listOfFiles])


def main():
    pass

if __name__ == "__main__":
    main()
