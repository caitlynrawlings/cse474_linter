todos:

- test the function that checks the rest of the file other than the header
- add tests for this

- check for if arg 1 is file or folder and if folder -> search recursively and run linter on each .ino file
- add tests for file/folder/not valid file

- add not-annoying tag that doesnt check for trailing spaces

- add check for indentations (spaces before line must be divisable by either 2 or 4)

current limitations:  

this block only records an error if there is one of these without having the corresponding section header above it somewhere in the code but does not handle if the case that the code is in the wrong section
`elif (not includes_found) and line.startswith("#include"):  
    res += [f"Line {num + 5}: Expected '// ================== Includes ==================' comment to define section"]  
elif (not defines_found) and line.startswith("#define"):  
    res += [f"Line {num + 5}: Expected '// =================== Macros ===================' comment to define section"]  
elif (not globals_found) and global_var_pattern.match(line):  
    res += [f"Line {num + 5}: Expected '// ============== Global Variables ==============' comment to define section"]  
elif (not prototypes_found) and function_prototype_pattern.match(line):  
    res += [f"Line {num + 5}: Expected '// ============= Function Prototypes ============' comment to define section"]`  


tests
    - header
        - correct no name param
        - correct with name parameter