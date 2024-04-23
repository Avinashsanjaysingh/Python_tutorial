# Write a program to sum a list with 4 numbers.

l1 = []

# defining the number of elements in the list l1
n = int(input("Enter the no. of elements in the list: "))

print("")

# taking the value in the list 'l1' (only input the int value)
for i in range(0,n):
    a = "Enter the marks of student no. " + str(i+1) + ": "
    a = int(input(a))
    l1.append(a)

print("\nThe list is:",l1)

# adding all the elements of the list
a = 0
for i in range(0,n):
    a += l1[i]

print("\nThe sum of the elements of the list is:",a)
