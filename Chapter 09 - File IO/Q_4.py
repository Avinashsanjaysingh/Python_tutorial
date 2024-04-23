# A file contains a word "Donkey" multiple times. you need to write a program which replaces this word with ###### by updating the same file.


with open("Q_4.txt", "r") as file:
    file_content = file.read().lower()

updated_content = file_content.replace("donkey", "######")

with open("Q_4.txt", "w") as file:
    file.write(updated_content)

# print("Word 'Donkey' replaced with '######' in the file.")





