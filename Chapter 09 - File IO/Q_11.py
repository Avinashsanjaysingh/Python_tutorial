# Write a python program to rename a file to "removed_by_python.txt".

import os

try:
    with open("Chapter 09 - File IO/New.txt", "r") as file:
        newFile = file.read()
except FileNotFoundError:
    with open("Chapter 09 - File IO/New.txt", "w") as file:
        file.write

os.rename("Chapter 09 - File IO/New.txt", "Chapter 09 - File IO/new.txt")


