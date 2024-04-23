# Write a program to find whether a given number is prime or not.

x = int(input("Enter the number: "))

def is_prime(x):
    for i in range(2,(int(x/2)+1)):
        if x%i == 0:
            return False
        return True

if is_prime(x):
    print("Prime")
else:
    print("not prime")




