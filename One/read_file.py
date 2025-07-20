# utils.py
def deco(color):
    def wrapper(func):
        def inner(*args, **kwargs):
            print(f"[{color.upper()}] --- START ---")
            result = func(*args, **kwargs)
            print(f"[{color.upper()}] --- END ---")
            return result
        return inner
    return wrapper

# reader.py
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
        try:
            with open(self._filename, 'r') as f:
                for line in f:
                    yield line.strip()
        except FileNotFoundError:
            print(f"File {self._filename} not found!")
            return

    def __str__(self):
        return f"FileReader for file: {self._filename}"

    def __add__(self, other):
        # создаёт новый объект с именем "file1+file2.txt"
        new_name = f"{self._filename.split('.')[0]}_{other.filename.split('.')[0]}.txt"
        try:
            with open(self._filename, 'r') as f1, open(other.filename, 'r') as f2, open(new_name, 'w') as fout:
                fout.write(f1.read())
                fout.write('\n')
                fout.write(f2.read())
            return FileReader(new_name)
        except FileNotFoundError as e:
            print(f"Error: {e}")
            return None

@deco("red")
def print_content(reader: FileReader):
    for line in reader.line_generator():
        print(line)

# child_reader.py
class MultiFileReader(FileReader):
    """Child class that can concatenate any number of files."""

    def __init__(self, filename):
        super().__init__(filename)  # вызывает конструктор родителя

    def concat_many(self, *filenames):
        new_name = "_".join(f.split('.')[0] for f in filenames) + ".txt"
        try:
            with open(new_name, 'w') as fout:
                for fname in filenames:
                    try:
                        with open(fname, 'r') as fin:
                            fout.write(fin.read())
                            fout.write('\n')
                    except FileNotFoundError:
                        print(f"Warning: File {fname} not found, skipping...")
            return FileReader(new_name)
        except Exception as e:
            print(f"Error creating combined file: {e}")
            return None

    def __str__(self):
        return f"MultiFileReader for file: {self.filename}"

class ChildFileReader(FileReader):
    def concat_files(self, *filenames: str) -> 'ChildFileReader':
        """Concatenates multiple files and creates a new file with combined content."""
        new_name = "combined_" + "_".join(f.split('.')[0] for f in filenames) + ".txt"
        try:
            with open(new_name, 'w') as fout:
                for filename in filenames:
                    try:
                        with open(filename, 'r') as f:
                            fout.write(f.read())
                            fout.write('\n')
                    except FileNotFoundError:
                        print(f"Warning: File {filename} not found, skipping...")
            return ChildFileReader(new_name)
        except Exception as e:
            print(f"Error creating combined file: {e}")
            return None

    def line_generator(self):
        """Overrides the parent generator to yield only non-empty lines."""
        try:
            with open(self._filename, 'r') as f:
                for line in f:
                    line = line.strip()
                    if line:  # only non-empty lines
                        yield line
        except FileNotFoundError:
            print(f"File {self._filename} not found!")
            return

# Test functions
def test_str():
    reader = FileReader("sample.txt")
    assert str(reader) == "FileReader for file: sample.txt"
    print("test_str() passed!")

def demo_functionality():
    """Demonstrate the functionality with sample files"""
    
    # Create sample files for demonstration
    print("Creating sample files...")
    
    with open("file1.txt", "w") as f:
        f.write("This is file 1\nLine 2 of file 1\n\nEmpty line above")
    
    with open("file2.txt", "w") as f:
        f.write("This is file 2\nLine 2 of file 2")
    
    with open("sample.txt", "w") as f:
        f.write("Sample file content\nLine 2\nLine 3")
    
    print("\n--- Testing FileReader ---")
    reader = FileReader("sample.txt")
    print(f"Reader: {reader}")
    
    print("\n--- Testing print_content with decorator ---")
    print_content(reader)
    
    print("\n--- Testing file addition ---")
    reader1 = FileReader("file1.txt")
    reader2 = FileReader("file2.txt")
    combined_reader = reader1 + reader2
    if combined_reader:
        print(f"Combined reader: {combined_reader}")
        print("Combined content:")
        print_content(combined_reader)
    
    print("\n--- Testing MultiFileReader ---")
    multi_reader = MultiFileReader("file1.txt")
    print(f"Multi reader: {multi_reader}")
    concatenated = multi_reader.concat_many("file1.txt", "file2.txt")
    if concatenated:
        print("Concatenated content:")
        print_content(concatenated)
    
    print("\n--- Testing ChildFileReader (non-empty lines only) ---")
    child_reader = ChildFileReader("file1.txt")
    combined_child = child_reader.concat_files("file1.txt", "file2.txt")
    if combined_child:
        print("ChildFileReader combined content (non-empty lines only):")
        for line in combined_child.line_generator():
            print(f"'{line}'")

# Run the tests and demo
if __name__ == "__main__":
    print("Running test...")
    test_str()
    
    print("\nRunning demonstration...")
    demo_functionality()