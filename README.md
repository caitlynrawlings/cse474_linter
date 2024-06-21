# Project Name

## About
Provide a brief description of your project, its purpose, and what problem it solves.

## Features
List the key features of your project.
- Feature 1
- Feature 2
- Feature 3

## Current Limitations
- Only records an error if there is something that should be in an includes, macros, global variables or function prototype sections without having the corresponding section header above it somewhere in the code but does not handle if the code is in the wrong section.
- Requires exact match for section separators (exact number of ====).

## Installation
Provide instructions on how to install and set up your project.
```sh
# Clone the repository
git clone https://github.com/yourusername/yourproject.git

# Navigate to the project directory
cd yourproject

# Install dependencies
pip install -r requirements.txt
```

## Usage
python linter.py <filename> [-n author_name]  
```sh
# Example usage for checking one file
python linter.py ./Lab1/Lab1Part2.ino
# Example usage for checking one file and specifying names to check for the author comment
python linter.py ./Lab1/Lab1Part2.ino -n "Student One, Student Two"
```

## Testing
Run `pytest` from top level directory

## Directory Structure
cse474_linter/  
├── README.md  
├── linter.py: the file with all the linter logic
├── tests/  
│   ├── test_files/: contains all the files used in the tests  
│   |── test_header.py: contains all the tests for checking the file header comment
|   └── test_seperation.py: contains tests for checking for comment for section seperators/headers at top of file
├── .gitignore
└── JOURNAL.md: Detailed log of the development process, including project updates, decisions, and challenges.

