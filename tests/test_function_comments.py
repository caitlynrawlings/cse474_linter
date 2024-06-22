# test_function.comments.py
import subprocess


# function before setup with correct name and description comment
def test_function_before_setup():
    result = subprocess.run(['python', 'linter.py', './tests/test_files/function_comment_tests/function_before_setup.ino'], capture_output=True, text=True)
    assert "./tests/test_files/function_comment_tests/function_before_setup.ino : No linter errors found\n" == result.stdout

# two functions before setup with correct name and description comment
def test_two_function_before_setup():
    result = subprocess.run(['python', 'linter.py', './tests/test_files/function_comment_tests/two_function_before_setup.ino'], capture_output=True, text=True)
    assert "./tests/test_files/function_comment_tests/two_function_before_setup.ino : No linter errors found\n" == result.stdout

# function before setup with incorrect name

# function before stup with no name

# function before setup with name but no description

# function before setup with name and empty description

# function befroe setup with no name or description

# function before setup with no name but description

# two functions before setup. first correct. second one wrong

# three functions before setup. first correct. second one wrong. third correct

# two functions before setup. first wrong. second correct

# two functions before setup. both wrong

