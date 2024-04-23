# Write a python program to print the contents of a directory using OS module. Search online for the function which does that.

'''
Certainly! You can use the `os` module in Python to list the contents of a directory. The `os` module provides a function called `os.listdir()`, which returns a list containing the names of the entries in the specified directory.

Here's a simple Python program that uses the `os` module to print the contents of a directory:

'''

import os

def print_directory_contents(directory_path):
    print(f"Contents of directory '{directory_path}':")
    try:
        # Get the list of entries in the directory
        entries = os.listdir(directory_path)

        # Print each entry
        for entry in entries:
            print(entry)

    except FileNotFoundError:
        print(f"Error: Directory '{directory_path}' not found.")

# Replace 'your_directory_path' with the path of the directory you want to inspect
directory_path = 'your_directory_path'
print_directory_contents(directory_path)


'''
Replace `'your_directory_path'` with the path of the directory you want to inspect. Save the script and run it using a Python interpreter. This program will print the contents of the specified directory.

Remember that the `os.listdir()` function returns both files and subdirectories, so the output will include both. You can customize the program further based on your specific requirements.
'''