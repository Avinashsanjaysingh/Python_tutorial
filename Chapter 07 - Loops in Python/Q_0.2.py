# Write a program to print the content of a list using while loop.

l = [1,2,3,4,5,6,7,'avinash','sumit','sanjay','kavita']

i = 0
while i < 11:
    print(l[i])
    i += 1

# if the list is taken from the user.
    
a = []
n = int(input("Enter the number of element: "))
m = n
while n > 0:
    b = input("Enter the element: ")
    a.append(b)
    n -= 1

j = 0
while j < m:
    print(a[j])
    j += 1
