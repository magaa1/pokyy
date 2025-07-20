class MultiFileReader(FileReader):
    """Child class that can concatenate any number of files."""

    def __init__(self, filename):
        super().__init__(filename)  # вызывает конструктор родителя

    def concat_many(self, *filenames):
        new_name = "_".join(filenames)
        with open(new_name, 'w') as fout:
            for fname in filenames:
                with open(fname, 'r') as fin:
                    fout.write(fin.read())
                    fout.write('\n')
        return FileReader(new_name)

    def __str__(self):
        return f"MultiFileReader for file: {self.filename}"


from src.reader import FileReader

class ChildFileReader(FileReader):
    def concat_files(self, *filenames: str) -> 'ChildFileReader':
        """Concatenates multiple files and creates a new file with combined content."""
        new_name = "combined_" + "_".join(f.split('.')[0] for f in filenames) + ".txt"
        with open(new_name, 'w') as fout:
            for filename in filenames:
                with open(filename, 'r') as f:
                    fout.write(f.read())
                    fout.write('\n')
        return ChildFileReader(new_name)

    def line_generator(self):
        """Overrides the parent generator to yield only non-empty lines."""
        with open(self._filename, 'r') as f:
            for line in f:
                line = line.strip()
                if line:  # only non-empty lines
                    yield line

