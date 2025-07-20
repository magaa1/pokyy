from src.utils import deco

class FileReader:
    def __init__(self, filename):
        self._filename = filename

    @property
    def filename(self):
        return self._filename

    @filename.setter
    def filename(self, value):
        self._filename = value

    def line_generator(self):
        with open(self._filename, 'r') as f:
            for line in f:
                yield line.strip()

    def __str__(self):
        return f"FileReader for file: {self._filename}"

    def __add__(self, other):
        # создаёт новый объект с именем "file1+file2.txt"
        new_name = f"{self._filename}_{other.filename}"
        with open(self._filename, 'r') as f1, open(other.filename, 'r') as f2, open(new_name, 'w') as fout:
            fout.write(f1.read())
            fout.write('\n')
            fout.write(f2.read())
        return FileReader(new_name)

@deco("red")
def print_content(reader: FileReader):
    for line in reader.line_generator():
        print(line)
from src.reader import FileReader 
