# Write a program to input eight numbers from the user and display all unique numbers(once).

a = set()

b = int(input("\nEnter the no of numbers you want to input: "))
print("")

for i in range(0,b):
    print("Enter the value no.", i+1,": ", end='')
    c = int(input(""))
    a.add(c)

print("\nTotal number of unique input is:",len(a),"\n\t\t   and they are:",a,"\n")


