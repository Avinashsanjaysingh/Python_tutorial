'''
    Write a program to count the number of zeroes in the following tuple:
        a=(7,0,8,0,0,9)
'''


l1 = []

n = int(input("Enter the no. of elements in the list: "))

print("")

for i in range(0,n):
    a = "Enter the marks of student no. " + str(i+1) + ": "
    a = int(input(a))
    l1.append(a)

print("\nThe list is:",l1)

a = 0
a = l1.count(0)
print("\nThe number of zeroes in the list is:",a)

