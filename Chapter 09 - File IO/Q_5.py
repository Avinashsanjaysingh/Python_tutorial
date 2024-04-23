# Repeat program 4 for a list of such words to be censored.

a = ['donkey','dog', 'bitch']

for word in a:
    # print(word)
    with open("Chapter 09 - File IO/Q_4.txt", "r") as file:
        file_content = file.read().lower()

    updated_content = file_content.replace(word, "######")
    
    with open("Chapter 09 - File IO/Q_4.txt", "w") as file:
        file.write(updated_content)


