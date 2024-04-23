'''
    We are going to write a program that generates a random number and asks the user to guess it.
    If the player's guess is higher than the actual number, the program displays "Lower number please". Similarly if the user's guess is too low, the program prints "higher number please".
    When the user guesses the correct number, the program displays the number of guesses the player used to arrive at the number.

'''

import random
    
a = random.randint(1,1000) 

b = int(input("\nGuess any number between 0 to 1000: "))

if a == b:
    print("\nYou guessed the correct number.\n")
elif a < b:
    print("\nYou guessed a higher number.\n")
else:
    print("\nYou guessed a lower number.\n")


    