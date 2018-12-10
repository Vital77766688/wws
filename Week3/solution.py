class FileReader:

    def __init__(self, filename = None):
        self.filename = filename

    def read(self):
        try:
            with open(self.filename) as f:
                res = f.read()
        except IOError:
            res = ""
        finally:
            return res

if __name__ == '__main__':
    reader = FileReader("example.txt")
    print(reader.read())