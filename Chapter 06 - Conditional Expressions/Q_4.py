# Write a program to find whether a given username contains less than 10 characters or not.


a = input("Enter your user name: ")
b = len(a)
if b < 10:
    print("Your username contains less than 10 characters.")
else:
    print("Username does not contains less than 10 characters.")


