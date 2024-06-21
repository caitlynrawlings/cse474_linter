# test_seperation.py
import subprocess

# includes tests
def test_includes_seperator():
    result = subprocess.run(['python', 'linter.py', './tests/test_files/seperation_tests/includes_seperator.ino'], capture_output=True, text=True)
    assert "./tests/test_files/seperation_tests/includes_seperator.ino : No linter errors found\n" == result.stdout

def test_no_includes_seperator():
    result = subprocess.run(['python', 'linter.py', './tests/test_files/seperation_tests/no_includes_seperator.ino'], capture_output=True, text=True)
    assert "./tests/test_files/seperation_tests/no_includes_seperator.ino\nLine 6: Expected '// ================== Includes ==================' comment to define section\n\n" == result.stdout

# macros tests
def test_macros_seperator():
    result = subprocess.run(['python', 'linter.py', './tests/test_files/seperation_tests/macros_seperator.ino'], capture_output=True, text=True)
    assert "./tests/test_files/seperation_tests/macros_seperator.ino : No linter errors found\n" == result.stdout

def test_no_macros_seperator():
    result = subprocess.run(['python', 'linter.py', './tests/test_files/seperation_tests/no_macros_seperator.ino'], capture_output=True, text=True)
    assert "./tests/test_files/seperation_tests/no_macros_seperator.ino\nLine 6: Expected '// =================== Macros ===================' comment to define section\n\n" == result.stdout

# globals tests
def test_globals_int_seperator():
    result = subprocess.run(['python', 'linter.py', './tests/test_files/seperation_tests/globals_int_seperator.ino'], capture_output=True, text=True)
    assert "./tests/test_files/seperation_tests/globals_int_seperator.ino : No linter errors found\n" == result.stdout

def test_no_globals_int_seperator():
    result = subprocess.run(['python', 'linter.py', './tests/test_files/seperation_tests/no_globals_int_seperator.ino'], capture_output=True, text=True)
    assert "./tests/test_files/seperation_tests/no_globals_int_seperator.ino\nLine 6: Expected '// ============== Global Variables ==============' comment to define section\n\n" == result.stdout

def test_no_globals_seperator_mult():
    result = subprocess.run(['python', 'linter.py', './tests/test_files/seperation_tests/no_globals_seperator_mult.ino'], capture_output=True, text=True)
    assert "./tests/test_files/seperation_tests/no_globals_seperator_mult.ino\nLine 7: Expected '// ============== Global Variables ==============' comment to define section\nLine 9: Expected '// ============== Global Variables ==============' comment to define section\nLine 10: Expected '// ============== Global Variables ==============' comment to define section\n\n" == result.stdout

# prototype tests
def test_prototype_seperator():
    result = subprocess.run(['python', 'linter.py', './tests/test_files/seperation_tests/prototype_seperator.ino'], capture_output=True, text=True)
    assert "./tests/test_files/seperation_tests/prototype_seperator.ino : No linter errors found\n" == result.stdout

def test_no_prototype_seperator():
    result = subprocess.run(['python', 'linter.py', './tests/test_files/seperation_tests/no_prototype_seperator.ino'], capture_output=True, text=True)
    assert "./tests/test_files/seperation_tests/no_prototype_seperator.ino\nLine 6: Expected '// ============= Function Prototypes ============' comment to define section\n\n" == result.stdout

# other tests
def test_define_in_wrong_section():
    result = subprocess.run(['python', 'linter.py', './tests/test_files/seperation_tests/define_after_includes.ino'], capture_output=True, text=True)
    assert "./tests/test_files/seperation_tests/define_after_includes.ino : No linter errors found\n" == result.stdout
