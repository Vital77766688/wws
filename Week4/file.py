from tempfile import gettempdir
from os.path import join

class File:

    def __init__(self, filename):
        self.filename = filename

    def __add__(self, other):
        with open(self.filename, 'r') as f:
            first = f.read()
        with open(other.filename, 'r') as f:
            second = f.read()
        new = first + second
        new_path = join(gettempdir(), "new_file")
        with open (new_path, 'w') as f:
            f.write(new)
        return File(new_path)

    def __str__(self):
        return self.filename

    def __iter__(self):
        pass

    def __next__(self):
        pass

    def write(self, text):
        with open(self.filename, 'w') as f:
            f.write(text)


if __name__ == '__main__':

    first = File("1.txt")
    second = File("2.txt")

    first.write("wws yoptvayumat\n")
    second.write("ya ebal\n")

    new = first + second


    print(type(new))
    print(new)
    for l in new:
        print(l)