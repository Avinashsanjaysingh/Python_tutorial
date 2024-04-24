# Write a program to make a copy of a text file "this.txt".


with open("Chapter 09 - File IO/Q_10.txt", "r") as file:
    File = file.read()

with open("Chapter 09 - File IO/Q_08.txt", "w") as file:
    newFile = file.write(File)
