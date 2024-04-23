# Write a python function which converts inches to cms.

def inchesToCm(inches):
    return inches*2.54

inches = int(input("Enter the length in inches: "))

cm = inchesToCm(inches)

print(f"{inches}inch = {cm}cm")

