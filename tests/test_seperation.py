# test_seperation.py
import subprocess

def test_too_short():
    result = subprocess.run(['python', 'linter.py', 'tests/test_files/header_tests/three_lines.ino'], capture_output=True, text=True)
    assert "tests/test_files/header_tests/three_lines.ino\nError: File should have at least four lines in it for header comment.\n\n" == result.stdout
