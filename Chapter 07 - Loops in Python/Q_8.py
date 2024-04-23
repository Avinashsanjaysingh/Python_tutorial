'''
Write a program to print the following star pattern:

            *
            **
            ***     (for n = 3)
'''

n = int(input("Enter the number: "))

while n < 1:
   n = int(input("The value of n should be greater or equal to 1.\nEnter the value of n: "))

for i in range(0,n+1):
    for j in range(0,i):
        print("*",end=' ')
    print("\n")





