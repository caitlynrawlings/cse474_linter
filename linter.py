import sys
import os
import re

# Checks the first four lines of file for header comment
# Parameters:
#   - lines: arrays of strings. each line is line from a file in order
#   - file_name: file name
#   - author_name: name to check for the Author comment. If None then checks not author is not empty.
#       Defaults to None
def check_file_header(lines, file_name, author_name=None):
    # Check the first line
    if len(lines) < 4:
        return ["Error: File should have at least four lines in it for header comment."]
    
    res = []
    expected_first_line = f"// Filename: {file_name}"
    if lines[0] != expected_first_line:
        res += [f"Line 1: Expected '{expected_first_line}' as the first comment line. Got '{lines[0]}'"]


    # Check the second line
    expected_second_line = "// Author: "

    # If author_name is provided, check if it matches
    if author_name:
        author_line = lines[1][len(expected_second_line):].strip()
        if author_name != author_line:
            res += [f"Line 2: Expected '{author_name}' in the Author line. Got '{author_line.strip()}'"]
    elif not lines[1].startswith(expected_second_line):
        res += [f"Line 2: Second line should start with '{expected_second_line}'. Got '{lines[1].strip()}'"]
    # If no author_name provided, check if the line is not empty
    elif lines[1].strip() == "// Author:":
        res += ["Line 2: Author name cannot be empty."]

    # Check the third line
    expected_third_line = "// Date: "
    if not lines[2].startswith(expected_third_line):
        res += [f"Line 3: Third line should start with '{expected_third_line}'. Got '{lines[2].strip()}'"]
    # check if the line is not empty
    elif lines[2].strip() == "// Date:":
        res += ["Line 3: Date cannot be empty."]

    # Check the fourth line
    expected_fourth_line = "// Description: "
    if not lines[3].startswith(expected_fourth_line):
        res += [f"Line 4: Fourth line should start with '{expected_fourth_line}'. Got '{lines[3].strip()}'"]
    # check if the line is not empty
    elif lines[3].strip() == "// Description:":
        res += ["Line 4: Description cannot be empty."]

    return res

# Checks above setup except for the header
# Parameters:
#   - lines: arrays of strings. each line is line from a file in order
def check_above_setup(lines):
    setup_found : bool = False
    loop_found : bool = False

    includes_found : bool = False
    defines_found : bool = False
    globals_found : bool = False
    prototypes_found : bool = False

    func_name_found : bool = False
    func_name = ""
    func_def_found : bool = False

    # Regular expression patterns to match global variables
    global_var_pattern = re.compile(r"^\s*(int|float|double|char|bool|long|short|unsigned|static\s+\w+(\w*\d*)*|\w*\s*\**)\s(\**)+\w+(\s*\[.*\])?\s*(=\s*[^;]+)?;\s*(//.*)?$")
    # Regular expression patterns to match function prototypes
    function_prototype_pattern = re.compile(r"^\s*\w+(\w*\d*)*(\s*\**+\s*\**)?\s+\w+\s*\([^;]*\)[^;]*;")
    # Regular expression patterns to match function declarations
    function_declaration_pattern = re.compile(r"(^\s*)(\w+(?: \w*\d*)*)(\s*\**+\s*\**)?\s+(\w+)\s*\(")

    lines = lines[4:] # skip first four lines because they were checked in header check
    res = []
    # check line by line
    for num, line in enumerate(lines):
        if not setup_found:
            if line.startswith("void setup()"):
                setup_found = True

            # only need to do the two checks below before setup is found

            # Check for includes, defines, globals, and prototypes
            elif (not includes_found) and line.startswith("#include"):
                res += [f"Line {num + 5}: Expected '// ================== Includes ==================' comment to define section"]
            elif (not defines_found) and line.startswith("#define"):
                res += [f"Line {num + 5}: Expected '// =================== Macros ===================' comment to define section"]
            elif (not globals_found) and global_var_pattern.match(line):
                res += [f"Line {num + 5}: Expected '// ============== Global Variables ==============' comment to define section"]
            elif (not prototypes_found) and function_prototype_pattern.match(line):
                res += [f"Line {num + 5}: Expected '// ============= Function Prototypes ============' comment to define section"]
            
            # Update flags based on comments indicating sections
            elif line.startswith("// ================== Includes =================="):
                includes_found = True
            elif line.startswith("// =================== Macros ==================="):
                defines_found = True
            elif line.startswith("// ============== Global Variables =============="):
                globals_found = True
            elif line.startswith("// ============= Function Prototypes ============"):
                prototypes_found = True
            elif not loop_found and line.startswith("void loop()"):
                    loop_found = True
        elif not loop_found:
            if line.startswith("void loop()"):
                loop_found = True
        # else -> both loop and setup have been found so just check rest of code 
        # for function description and names and trailing white spaces

        # Check for function descriptions and match function names
        # This get checks for each line (both before and after setup() found)
        if func_name_found:
            if not func_def_found:
                # expect the next line after function name comment to be definition name comment
                if not line.startswith("// Description: "):
                    res += [f"Line {num + 5}: Expected line to start with '// Description: ' to describe function"]
                    func_name_found = False
                else:
                    func_def_found = True
                    # todo: add check for description not being empty
            elif function_declaration_pattern.match(line):
                # both function comments and function found
                # reset variables
                func_def_found = False
                func_name_found = False

                # check if the func_name mathes the function name in the function declaration
                match = function_declaration_pattern.match(line)
                func_name_in_declaration = match.group(4) if match else None
                if func_name_in_declaration != func_name:
                    res += [f"Line {num + 5}: Function name '{func_name_in_declaration}' does not match the declared function name '{func_name}'"]

            # else could be comments of more of the description so don't do anything
        elif line.startswith("// Name: "):
            # get the rest of the line and cut off trailing whitespace and save that to func_name 
            func_name = line[len("// Name: "):].strip()
            func_name_found = True
        elif function_declaration_pattern.match(line) and not function_prototype_pattern.match(line) and (not line.startswith("void loop()")) and (not line.startswith("void setup()")):
            res += [f"Line {num + 5}: Expected to find '// Name: ' and '// Description: ' comments for function"]


        # check each line for trailing whitespace
        if line != line.rstrip():
            res += [f"Line {num + 5}: Trailing whitespace"]

    return res

# checks all rules on one file
def check_file(file_path, author_name=None):
    try:
        with open(file_path, 'r') as file:
            lines = [line.strip('\n') for line in file.readlines()]
            errors = check_file_header(lines, os.path.basename(file.name), author_name)
            errors += check_above_setup(lines)
            if len(errors) == 0:
                return f"{file_path} : No linter errors found"
            else:
                return f"{file_path}\n" + '\n'.join(errors) + '\n'
    except FileNotFoundError:
        return f"Error: File '{file_path}' not found."
            

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python linter.py <filename> [-n author_name]")
        sys.exit(1)

    file_path = sys.argv[1]
    author_name = None
    
    if len(sys.argv) == 4 and sys.argv[2] == "-n":
        author_name = sys.argv[3]

    print(check_file(file_path, author_name))
