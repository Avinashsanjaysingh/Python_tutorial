# Write a program to mine a log file and find out whether it contains 'python'.

with open("Chapter 09 - File IO/test.txt","r") as file:
    file_content = file.read().lower()

# x = file_content.find("python")
# if x >= 0:
#     print("The log file contains python.")

if 'python' in file_content:
    print("The log file contains 'python'.")



