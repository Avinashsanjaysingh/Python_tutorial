# Create an empty dictionary. Allow 4 friends to enter their favourite language as values and use keys as their names. Assume that the names are unique.

d = {}

n = int(input("\nEnter the number of entries: "))

for n in range(0,n):
    print("")
    a = input("Enter your name: ")
    b = input("Enter your favourite language: ")
    d[a] = b
    # d.update({a:b})

print("")

for x, y in d.items():
    print(f"{x}: {y}")

print("")

# i = d.items()
# print("\n",i,"\n")

'''
# f-string or formatted string
name = "Alice"
age = 30

# Using f-string to embed variables in a string
message = f"My name is {name} and I am {age} years old."

print(message)

'''
