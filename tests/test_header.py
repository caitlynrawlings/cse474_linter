# test_header.py
import subprocess

def test_too_short():
    result = subprocess.run(['python', 'linter.py', 'tests/test_files/header_tests/three_lines.ino'], capture_output=True, text=True)
    assert "tests/test_files/header_tests/three_lines.ino\nError: File should have at least four lines in it for header comment.\n\n" == result.stdout

def test_valid_file_header():
    result = subprocess.run(['python', 'linter.py', 'tests/test_files/header_tests/correct_header.ino'], capture_output=True, text=True)
    assert "tests/test_files/header_tests/correct_header.ino : No linter errors found\n" == result.stdout

def test_valid_file_header_name_tag():
    result = subprocess.run(['python', 'linter.py', 'tests/test_files/header_tests/correct_header.ino', '-n', 'John Doe'], capture_output=True, text=True)
    assert "tests/test_files/header_tests/correct_header.ino : No linter errors found\n" == result.stdout

def test_wrong_filename():
    result = subprocess.run(['python', 'linter.py', 'tests/test_files/header_tests/wrong_filename.ino'], capture_output=True, text=True)
    assert "tests/test_files/header_tests/wrong_filename.ino\nLine 1: Expected '// Filename: wrong_filename.ino' as the first comment line. Got '// Filename: filename.ino'\n\n" == result.stdout

def test_no_filename():
    result = subprocess.run(['python', 'linter.py', 'tests/test_files/header_tests/no_filename.ino'], capture_output=True, text=True)
    assert "tests/test_files/header_tests/no_filename.ino\nLine 1: Expected '// Filename: no_filename.ino' as the first comment line. Got '// this should be the filename'\n\n" == result.stdout

def test_wrong_author_name():
    result = subprocess.run(['python', 'linter.py', 'tests/test_files/header_tests/correct_header.ino', '-n', 'Author Wrong'], capture_output=True, text=True)
    assert "tests/test_files/header_tests/correct_header.ino\nLine 2: Expected 'Author Wrong' in the Author line. Got 'John Doe'\n\n" == result.stdout

def test_empty_author_line():
    result = subprocess.run(['python', 'linter.py', 'tests/test_files/header_tests/empty_author.ino'], capture_output=True, text=True)
    assert "tests/test_files/header_tests/empty_author.ino\nLine 2: Author name cannot be empty.\n\n" == result.stdout

def test_space_author():
    result = subprocess.run(['python', 'linter.py', 'tests/test_files/header_tests/space_author.ino'], capture_output=True, text=True)
    assert "tests/test_files/header_tests/space_author.ino\nLine 2: Author name cannot be empty.\n\n" == result.stdout

def test_no_author():
    result = subprocess.run(['python', 'linter.py', 'tests/test_files/header_tests/no_author.ino'], capture_output=True, text=True)
    assert "tests/test_files/header_tests/no_author.ino\nLine 2: Second line should start with '// Author: '. Got '// this is where the author should be'\n\n" == result.stdout

def test_empty_date():
    result = subprocess.run(['python', 'linter.py', 'tests/test_files/header_tests/empty_date.ino'], capture_output=True, text=True)
    assert "tests/test_files/header_tests/empty_date.ino\nLine 3: Date cannot be empty.\n\n" == result.stdout

def test_no_date():
    result = subprocess.run(['python', 'linter.py', 'tests/test_files/header_tests/no_date.ino'], capture_output=True, text=True)
    assert "tests/test_files/header_tests/no_date.ino\nLine 3: Third line should start with '// Date: '. Got '// this is where the date should be'\n\n" == result.stdout

def test_empty_description():
    result = subprocess.run(['python', 'linter.py', 'tests/test_files/header_tests/empty_description.ino'], capture_output=True, text=True)
    assert "tests/test_files/header_tests/empty_description.ino\nLine 4: Description cannot be empty.\n\n" == result.stdout

def test_no_description():
    result = subprocess.run(['python', 'linter.py', 'tests/test_files/header_tests/no_description.ino'], capture_output=True, text=True)
    assert "tests/test_files/header_tests/no_description.ino\nLine 4: Fourth line should start with '// Description: '. Got '// this is where the description should be'\n\n" == result.stdout
