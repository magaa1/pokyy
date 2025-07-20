from src.reader import FileReader, print_content

def test_str():
    reader = FileReader("sample.txt")
    assert str(reader) == "FileReader for file: sample.txt"
