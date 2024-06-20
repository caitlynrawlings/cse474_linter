# test_header.py
import subprocess

def test_too_short():
    result = subprocess.run(['python', 'linter.py', 'tests/test_files/header_tests/three_lines.ino'], capture_output=True, text=True)
    assert "Error: File should have at least four lines in it for header comment." in result.stdout

def test_valid_file_header():
    result = subprocess.run(['python', 'linter.py', 'tests/test_files/header_tests/correct_header.ino'], capture_output=True, text=True)
    assert "File header check passed." in result.stdout

def test_valid_file_header_name_tag():
    result = subprocess.run(['python', 'linter.py', 'tests/test_files/header_tests/correct_header.ino', '-n', 'John Doe'], capture_output=True, text=True)
    assert "File header check passed." in result.stdout

def test_wrong_filename():
    result = subprocess.run(['python', 'linter.py', 'tests/test_files/header_tests/wrong_filename.ino'], capture_output=True, text=True)
    assert "Error: Expected '// Filename: wrong_filename.ino' as the first comment line. Got '// Filename: filename.ino'" in result.stdout

def test_no_filename():
    result = subprocess.run(['python', 'linter.py', 'tests/test_files/header_tests/no_filename.ino'], capture_output=True, text=True)
    assert "Error: Expected '// Filename: no_filename.ino' as the first comment line. Got '// this should be the filename'" in result.stdout

def test_wrong_author_name():
    result = subprocess.run(['python', 'linter.py', 'tests/test_files/header_tests/correct_header.ino', '-n', 'Author Wrong'], capture_output=True, text=True)
    assert "Error: Expected 'Author Wrong' in the Author line. Got 'John Doe'" in result.stdout

def test_empty_author_line():
    result = subprocess.run(['python', 'linter.py', 'tests/test_files/header_tests/empty_author.ino'], capture_output=True, text=True)
    assert "Error: Author name cannot be empty." in result.stdout

def test_space_author():
    result = subprocess.run(['python', 'linter.py', 'tests/test_files/header_tests/space_author.ino'], capture_output=True, text=True)
    assert "Error: Author name cannot be empty." in result.stdout

def test_no_author():
    result = subprocess.run(['python', 'linter.py', 'tests/test_files/header_tests/no_author.ino'], capture_output=True, text=True)
    assert "Error: Second line should start with '// Author: '. Got '// this is where the author should be'" in result.stdout

def test_empty_date():
    result = subprocess.run(['python', 'linter.py', 'tests/test_files/header_tests/empty_date.ino'], capture_output=True, text=True)
    assert "Error: Date cannot be empty." in result.stdout

def test_no_date():
    result = subprocess.run(['python', 'linter.py', 'tests/test_files/header_tests/no_date.ino'], capture_output=True, text=True)
    assert "Error: Third line should start with '// Date: '. Got '// this is where the date should be'" in result.stdout

def test_empty_description():
    result = subprocess.run(['python', 'linter.py', 'tests/test_files/header_tests/empty_description.ino'], capture_output=True, text=True)
    assert "Error: Description cannot be empty." in result.stdout

def test_no_description():
    result = subprocess.run(['python', 'linter.py', 'tests/test_files/header_tests/no_description.ino'], capture_output=True, text=True)
    assert "Error: Fourth line should start with '// Description: '. Got '// this is where the description should be'" in result.stdout
