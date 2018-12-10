import tempfile
import os

class File:

    def __init__(self, filepath):
        self.filepath = filepath
        if not os.path.isfile(filepath):
            f = open(filepath, 'w')
            f.close()
        self.file = open(filepath, 'r+')

    def __del__(self):
        self.file.close()

    def __str__(self):
        return self.filepath

    def __add__(self, other):
        self.file.seek(0)
        other.file.seek(0)
        with open(os.path.join(tempfile.gettempdir(), "new_file.txt"), 'w') as f:
            f.write(self.file.read() + other.file.read())
        return File(os.path.join(tempfile.gettempdir(), "new_file.txt"))

    def __iter__(self):
        return self

    def __next__(self):
        line = self.file.readline()
        if line == '':
            raise StopIteration
        return line

    def write(self, string):
        self.file.write(string)

if __name__ == '__main__':

    first = File(os.path.join(tempfile.gettempdir(), 'first'))
    second = File(os.path.join(tempfile.gettempdir(), 'second'))

    first.write("123\n")
    second.write("321\n")

    new_obj = first + second

    print(new_obj)

    for line in new_obj:
        print(line)