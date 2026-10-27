# File Existence Checker
# Write a Python script that:
# Accepts a filename as a command-line argument
# Checks if the file exists
# Checks if it is a file
# Checks if it is a directory
# If the file exists, checks if it is readable, writable, and executable
# Prints appropriate messages for each check
# Handles the case where no argument is provided
# Hint: Use os.R_OK, os.W_OK, os.X_OK, and os.F_OK to check file access permissions.

import os, sys

if len(sys.argv) < 2:
    print(f'USE: python file_checker.py <file>')
    sys.exit(1)

file = sys.argv[1]
if os.access(file, os.F_OK):
    print(f'{file} exists')
    if os.path.isfile(file):
        print(f'{file} is a file')
    elif os.path.isdir(file):
        print(f'{file} is a directory')

    if os.access(file, os.R_OK):
        print(f'{file} is readable')
    else:
        print(f'{file} is not readable')

    if os.access(file, os.W_OK):
        print(f'{file} is writable')
    else:
        print(f'{file} is not writable')

    if os.access(file, os.X_OK):
        print(f'{file} is executable')
    else:
        print(f'{file} is not executable')

else:
    print(f'{file} does not exist')