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
def test_wrong_name_before_setup():
    result = subprocess.run(['python', 'linter.py', './tests/test_files/function_comment_tests/wrong_name.ino'], capture_output=True, text=True)
    assert "./tests/test_files/function_comment_tests/wrong_name.ino\nLine 21: Function name 'updateCounter' does not match the commented function name 'wrongName'\n\n" == result.stdout

# function with multiline description
def test_multiline_description():
    result = subprocess.run(['python', 'linter.py', './tests/test_files/function_comment_tests/multiline_description.ino'], capture_output=True, text=True)
    assert "./tests/test_files/function_comment_tests/multiline_description.ino : No linter errors found\n" == result.stdout

# function before setup with no name
def test_no_name():
    result = subprocess.run(['python', 'linter.py', './tests/test_files/function_comment_tests/no_name.ino'], capture_output=True, text=True)
    assert "./tests/test_files/function_comment_tests/no_name.ino\nLine 8: Expected to find '// Name: ' and '// Description: ' comments for function\n\n" == result.stdout

# function befroe setup with no name or description
def test_no_name_no_desc():
    result = subprocess.run(['python', 'linter.py', './tests/test_files/function_comment_tests/no_name_no_desc.ino'], capture_output=True, text=True)
    assert "./tests/test_files/function_comment_tests/no_name_no_desc.ino\nLine 9: Expected to find '// Name: ' and '// Description: ' comments for function\n\n" == result.stdout

# function before setup with name but no description
def test_no_desc():
    result = subprocess.run(['python', 'linter.py', './tests/test_files/function_comment_tests/two_no_desc.ino'], capture_output=True, text=True)
    assert "./tests/test_files/function_comment_tests/two_no_desc.ino\nLine 8: Expected line to start with '// Description: ' to describe function\nLine 15: Expected line to start with '// Description: ' to describe function\n\n" == result.stdout

# function before setup with name and empty description
def test_empty_descriptions():
    result = subprocess.run(['python', 'linter.py', './tests/test_files/function_comment_tests/empty_descriptions.ino'], capture_output=True, text=True)
    assert "./tests/test_files/function_comment_tests/empty_descriptions.ino\nLine 7: Function description cannot be empty\nLine 7: Trailing whitespace\n\n" == result.stdout

# three functions before setup. first correct. second one wrong. third correct
def test_right_wrong_right():
    result = subprocess.run(['python', 'linter.py', './tests/test_files/function_comment_tests/right_wrong_right.ino'], capture_output=True, text=True)
    assert "./tests/test_files/function_comment_tests/right_wrong_right.ino\nLine 13: Expected line to start with '// Description: ' to describe function\nLine 14: Function name 'anotherFunction' does not match the commented function name 'wrongName'\n\n" == result.stdout

# two functions before setup. first wrong. second correct
def test_wrong_right():
    result = subprocess.run(['python', 'linter.py', './tests/test_files/function_comment_tests/wrong_right.ino'], capture_output=True, text=True)
    assert "./tests/test_files/function_comment_tests/wrong_right.ino\nLine 8: Expected line to start with '// Description: ' to describe function\nLine 8: Function name 'anotherFunction' does not match the commented function name 'wrongName'\n\n" == result.stdout


# functions after setup() and loop()

def test_after_loop1():
    result = subprocess.run(['python', 'linter.py', './tests/test_files/function_comment_tests/after_loop1.ino'], capture_output=True, text=True)
    assert "./tests/test_files/function_comment_tests/after_loop1.ino\nLine 13: Function description cannot be empty\nLine 13: Trailing whitespace\nLine 37: Function name 'anotherFunction' does not match the commented function name 'wrongName'\n\n" == result.stdout

def test_after_loop2():
    result = subprocess.run(['python', 'linter.py', './tests/test_files/function_comment_tests/after_loop2.ino'], capture_output=True, text=True)
    assert "./tests/test_files/function_comment_tests/after_loop2.ino\nLine 13: Function description cannot be empty\nLine 13: Trailing whitespace\nLine 37: Function name 'anotherFunction' does not match the commented function name 'wrongName'\nLine 61: Expected to find '// Name: ' and '// Description: ' comments for function\n\n" == result.stdout
