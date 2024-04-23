# Labell the program written in problem 4 with comments.

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