# Write a program to print multiplication table of n using for loop in reversed order.

n = int(input("Enter the value of n: "))

for i in range(0,10):
    j = 10-i
    print(n,"*",j,"=",n*j)


