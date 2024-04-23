# Write a program to find the sum of first n natural numbers using while loop.

n = int(input("Enter the value of n: "))
while n < 1:
    n = int(input("Enter the value of n: "))

i = 0
j = 0
while i <= n:
    j += i
    i += 1

print("The sum of first",n,"natural number is",j)


