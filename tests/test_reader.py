import os
from src.reader import FileReader

def test_line_generator(tmp_path):
    # создаём временный файл с контентом
    file = tmp_path / "sample.txt"
    file.write_text("line1\nline2\nline3")

    reader = FileReader(str(file))
    lines = list(reader.line_generator())

    assert lines == ["line1", "line2", "line3"]
