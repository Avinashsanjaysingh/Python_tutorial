'''
    Write a python function to print first n lines of the following pattern:

        * * *
        * *
        *           (for n = 3)
'''

def pattern(n):
    for i in range(n+1):
        for j in range(n-i):
            print("*",end=" ")
        print("\n")

n = int(input("Enter the lines, n: "))
print(pattern(n))

