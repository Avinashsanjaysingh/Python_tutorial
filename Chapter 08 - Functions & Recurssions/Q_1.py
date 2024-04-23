# Write a program using function to find greatest of three numbers.


def greatestAmongThree(num1, num2, num3):
    if ((num1 > num2) and (num1 > num3)):
        return f"{num1} is greatest"
    elif((num2 > num1) and (num2 >num3)):
        return f"{num2} is greatest"
    elif((num3 > num1) and (num3 >num2)):
        return f"{num3} is greatest"
    elif((num1 == num2) and (num1 == num3)):
        return f"All are equal"
    elif((num1 == num2) and (num1 > num3)):
        return f"{num1} & {num2} are greatest"
    elif((num1 > num2) and (num1 == num3)):
        return f"{num1} & {num3} are greatest"
    elif((num2 == num1) and (num2 > num3)):
        return f"{num1} & {num2} are greatest"
    elif((num2 > num1) and (num2 == num3)):
        return f"{num2} & {num3} are greatest"
    elif((num3 == num1) and (num3 > num2)):
        return f"{num1} & {num3} are greatest"
    elif((num3 > num1) and (num3 == num2)):
        return f"{num2} & {num3} are greatest"

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
num3 = int(input("Enter third number: "))

print(greatestAmongThree(num1,num2,num3))






'''
def is_prime(x):
    for i in range(2,x):
        if ((x%i) == 0):
            return False
    return True
    
x = int(input("Enter the number: "))
while x < 3:
   x = int(input("Enter the number: "))


if is_prime(x):
    print("Prime")
else:
    print("not prime")
'''

