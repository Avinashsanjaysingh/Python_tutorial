# Write a program to accept marks of 6 students and display them in a sorted manner.


l1 = []

n = int(input("Enter the number of Students: "))

for i in range(0,n):
    a = "Enter the marks of student no. " + str(i+1) + ": "
    a = int(input(a))
    l1.append(a)

l1.sort()

print(l1)

