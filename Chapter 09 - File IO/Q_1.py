# Write a program to read the text from a given file 'poems.txt' and find out whether it contains the word 'twinkle'.

def checkForTwinkle(word):
    try:
    # s = open("tet.txt","r").read()
        if word in open("Chapter 09 - File IO/test.txt","r").read().lower():
            print(f"This file contains '{word}'.")
        else:
            print(f"This file does not contain '{word}'.")
    except (FileNotFoundError):
        print("This file does not exist.")

print("\nCheck the word in the file 'test.txt'.\n")
word = input("Enter the word you want to check: ")

checkForTwinkle(word)



