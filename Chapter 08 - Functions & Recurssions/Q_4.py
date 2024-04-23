# Write a recursive function to calculate the sum of first n natural numbers.

def sumOfnNumbers(n):
    if n == 0:
        return 0
    else:
        return n + sumOfnNumbers(n-1)

print(sumOfnNumbers(2))

