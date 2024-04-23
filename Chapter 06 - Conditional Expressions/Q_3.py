'''
A spam comment is defined as a text containing following keywords:
        "make a lot of money", "buy now", "¸", "click this"
        write a program to detect these spams.

'''


c = input("Enter the comment: ")

match c:
    case "make a lot of money":
        print("This is a spam.")
    case "buy now":
        print("This is a spam.")
    case "buy now":
        print("This is a spam.")
    case "click this":
        print("This is a spam.")
    case  _:
        print("This is not spam.")


