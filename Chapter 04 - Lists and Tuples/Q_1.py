# Write a program to store seven fruits in a list entered by the user.

l1 = []

n = int(input("Enter the number of fruits: "))

# while n>0:
#     b = "Enter fruit's name: " + str(n) + " "
#     a = input(b)
#     l1.append(a)
#     n -= 1

for i in range(0,n):
    a = "Enter fruit's name: " + str(i+1) + ". "
    a = input(a)
    l1.append(a)

print(l1)



'''

l = [1,2,3]
print(l)
l.insert(0,2)
print(l)
l.extend(l)
print(l)
print(l[0:3])

'''