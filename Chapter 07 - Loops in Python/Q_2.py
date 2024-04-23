# Write a program to greet all the person names stored in a list l1 and which starts with S 
#        l1 = ["Avinash", "Soham", "Virat", "Suresh"]


l1 = ["Avinash", "Soham", "Virat", "Suresh"]

for i in range(0,4):
    a = l1[i]
    b = a.lower()
    c = b[0]
    if c == 's':
        print("Good Morning!",a)


