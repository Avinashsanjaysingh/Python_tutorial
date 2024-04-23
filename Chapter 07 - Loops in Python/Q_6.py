# Write a program to calculate the factorial of a given number using for loop.

a = int(input("Enter the number: "))
while a < 1:
    a = int(input("Enter the number: "))

i = 1
j = 1

while i <= a:
    j *= i
    i += 1

print("The factorial of",a,"is",j)

