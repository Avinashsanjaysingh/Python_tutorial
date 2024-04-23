# Write a program to create a dictionary of Hindi Words with values as their english translation. Provide user with an option to look it up!


dict = {'नमस्ते': 'Hello','प्यार': 'Love','खुशी': 'Happiness','गाड़ी': 'Car','आसमान': 'Sky',}

a = input("\nEnter the Hindi the word for English translation: ")

b = dict.get(a)

if b == None:
    print("\nSorry, We do not have the meaning of ",a)
else:
    print("\n",a ," --> ",b,"\n")




'''
a = {"b":1,"c":2,}
x = "b"
print(a[x])
a["d"] = 5
print(a)
print(a.keys())
print(a.values())
print(a.items())
print(type(a))

y = input("Enter the key: ")
z = a.get(y)
if z == None:
    print("sorry")
else:
    print(z)

'''


### Chatgpt generated

# # Create a dictionary of Hindi words and their English translations
# hindi_english_dict = {
#     'नमस्ते': 'Hello',
#     'प्यार': 'Love',
#     'खुशी': 'Happiness',
#     'गाड़ी': 'Car',
#     'आसमान': 'Sky',
#     # Add more words as needed
# }

# def lookup_translation():
#     # Get user input for the Hindi word
#     hindi_word = input("Enter a Hindi word to look up: ")

#     # Look up the translation in the dictionary
#     translation = hindi_english_dict.get(hindi_word)

#     # Display the result
#     if translation:
#         print(f"The English translation of '{hindi_word}' is: {translation}")
#     else:
#         print(f"Sorry, '{hindi_word}' not found in the dictionary.")

# # Main program loop
# while True:
#     print("\nHindi-English Dictionary:")
#     print("1. Look up a word")
#     print("2. Exit")

#     choice = input("Enter your choice (1 or 2): ")

#     if choice == '1':
#         lookup_translation()
#     elif choice == '2':
#         print("Exiting the program. Goodbye!")
#         break
#     else:
#         print("Invalid choice. Please enter 1 or 2.")