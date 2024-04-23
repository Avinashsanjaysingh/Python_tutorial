# Write a python program to print a table of a number which lies between 1 to 10.


a = int(input("Enter a number between 1 to 10: "))

def table(x):
    for i in range(1,11):
        print(x,"*",i,"=",x*i)

match a:
    case 1:
        table(1)
    case 2:
        table(2)
    case 3:
        table(3)
    case 4:
        table(4)
    case 5:
        table(5)
    case 6:
        table(6)
    case 7:
        table(7)
    case 8:
        table(8)
    case 9:
        table(9)
    case 10:
        table(10)
    case _:
        print("Pelase enter the number between 1 to 10.")

