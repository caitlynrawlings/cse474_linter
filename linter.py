import sys
import re
import os

def check_file_header(file, author_name=None):
    lines = [line.strip('\n') for line in file.readlines()]
    
    # Check the first line
    if len(lines) < 4:
        return "Error: File should have at least four lines in it for header comment."
    
    file_name_only = os.path.basename(file.name)
    expected_first_line = f"// Filename: {file_name_only}"
    if lines[0] != expected_first_line:
        return f"Error: Expected '{expected_first_line}' as the first comment line. Got '{lines[0]}'"

    # Check the second line
    expected_second_line = "// Author: "
    if not lines[1].startswith(expected_second_line):
        return f"Error: Second line should start with '{expected_second_line}'. Got '{lines[1].strip()}'"

    # If author_name is provided, check if it matches
    if author_name:
        author_line = lines[1][len(expected_second_line):].strip()
        if author_name != author_line:
            return f"Error: Expected '{author_name}' in the Author line. Got '{author_line.strip()}'"

    # If no author_name provided, check if the line is not empty
    elif lines[1].strip() == "// Author:":
        return "Error: Author name cannot be empty."

    # Check the third line
    expected_third_line = "// Date: "
    if not lines[2].startswith(expected_third_line):
        return f"Error: Third line should start with '{expected_third_line}'. Got '{lines[2].strip()}'"
    # check if the line is not empty
    if lines[2].strip() == "// Date:":
        return "Error: Date cannot be empty."

    # Check the fourth line
    expected_fourth_line = "// Description: "
    if not lines[3].startswith(expected_fourth_line):
        return f"Error: Fourth line should start with '{expected_fourth_line}'. Got '{lines[3].strip()}'"
    # check if the line is not empty
    if lines[3].strip() == "// Description:":
        return "Error: Description cannot be empty."

    return None

# checks above setup except for the header
# def check_above_setup(file):
#     setup_found : bool = False
#     loop_found : bool = False

#     lines = [line.strip('\n') for line in file.readlines()]
#     lines = [lines[4:]] # skip first four lines -> checked in header check
#     # Check the first line
#     if len(lines) == 0:
#         return "Error: File should have setup() and loop() function."
            
#     return None

# checks all rules on one file
def check_file(file_path, author_name=None):
    try:
        with open(file_path, 'r') as file:
            return check_file_header(file, author_name)
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

    lint_error = check_file(file_path, author_name)

    if lint_error:
        print(lint_error)
    else:
        print("File header check passed.")
