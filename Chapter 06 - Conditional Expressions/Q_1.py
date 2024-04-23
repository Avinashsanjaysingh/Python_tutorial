# Write a program to find greatest of four numbers entered by the user.

'''
# Using conditional expressions.

print()
a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))
c = int(input("Enter the third number: "))
d = int(input("Enter the fourth number: "))
print()

if (a >= b) and ((a >= c) and (a >= d)):
    print("The largest number is: ",a)
elif (b >= a) and ((b >= c) and (b >= d)):
    print("The largest number is: ",b)
elif (c >=a) and ((c >=b) and (c >= d)):
    print("The largest number is: ",c)
else:
    print("The largest number is: ",d)
'''


'''
# Using list method. This code can take any number of input for comparision and give the largest number as output.

print()
x = []

n = int(input("Enter the number of inputs: "))
print()

for i in range(0,n):
    j = int(input("Enter the number: "))
    x.append(j)

x.sort()
print("\nThe greatest number is:",x[-1],"\n")
'''


'''
# This was the first practice method.

if a>=b:
    if a>=c:
        if a>=d:
            print(a)
if b>=a:
    if b>=c:
        if b>=d:
            print(b)
if c>=a:
    if c>=b:
        if c>=d:
            print(c)
if d>=a:
    if d>=b:
        if d>=c:
            print(d)
'''
