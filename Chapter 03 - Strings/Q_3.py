# Write a program to detect double spaces in a string.


# a = 'hello' \     # '\' is used to write a multi line string.
#     'hii'         # ''' ''' is also used to write a multi line string.
# print(a)

a = input("Enter the string: ")

if "  " in a:
    print("There is double space in the string.")
else:
    print("There is no double space in the string.")