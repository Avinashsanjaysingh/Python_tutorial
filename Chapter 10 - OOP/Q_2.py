# Write a class calculator capable of finding square, cube and squareroot of a number.


import math

class Calculator:
    
    def __init__(self, number):
        self.number = number
        self.square = number ** 2
        self.cube = number ** 3
        self.sqrt = math.sqrt(number)

    def output(self):
        return f"\nNumber = {self.number}\nsquare = {self.square}\ncube = {self.cube}\nsquareroot = {self.sqrt}\n"
    
# calculation1 = Calculator(1)
# print(calculation1.output())

print(Calculator(5).output())

