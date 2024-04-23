# Stone paper Scissor Game

import random

print("\nWelcome to Rock Paper Scissor Game!")

a = int(input("\nSelect 1 for Rock, 2 for Paper & 3 for Scissor: "))

while a<1 or a>3:
    a = int(input("\nSelect 1 for Rock, 2 for Paper & 3 for Scissor: "))
 
if a == 1:
    print("\nYou selected Rock")
elif a == 2:
    print("\nYou selected Paper")
elif a == 3:
    print("\nYou Selected Scissor")

b = (1,2,3)
b = random.choice(b)

if b == 1:
    print("\nComputer selected Rock\n")
elif b == 2:
    print("\nComputer selected Paper\n")
elif b == 3:
    print("\nComputer selected Scissor\n")


if a == b:
    print("The match is tied.")
elif (a == 1 and b == 3) or (a == 2 and b == 1) or (a == 3 and b == 2):
    print("You Won!")
else:
    print("You lost")


