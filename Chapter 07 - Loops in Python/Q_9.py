'''
Write a program to print the following star pattern:

            * * *
            *   *
            * * *       (for n = 3)

'''

n = int(input("Enter the value of n: "))

while n < 3:
   n = int(input("The value of n should be greater or equal to 3.\nEnter the value of n: "))
 

for i in range(0,n):
    print("*",end='  ')
print("\n")
for k in range(0,n-2):
    for j in range(0,n):
        if ((j == 0) or (j == n-1)):
            print("*",end='  ')
        else:
            print(" ",end='  ')
    print("\n")
for i in range(0,n):
    print("*",end='  ')
print("\n")





