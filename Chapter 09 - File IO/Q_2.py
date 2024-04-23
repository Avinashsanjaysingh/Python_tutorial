# The game() function in a program lets a user play a game and returns the score as an integer. You need to read a file 'Hiscore.txt' which is either blank or contains the previous Hi-Score. You need to write a program to update the Hi-Score whenever game() breaks the Hi-Score.

import random

def game():
    return random.randint(1, 100)

try:
    with open("Hi-Score.txt", "r") as file:
        high_score_str = file.read().strip()
        if high_score_str:  # Check if the string is not empty
            HighScore = int(high_score_str)
        else:
            HighScore = 0  # Set default high score if file is empty
except FileNotFoundError:
    HighScore = 0
    with open("Hi-Score.txt", "w") as file:
        file.write(str(HighScore))

Score = game()

if Score <= HighScore:
    print(f"Your score is {Score} and the Hi-Score is {HighScore}.")
else:
    with open("Hi-Score.txt", "w") as file:
        file.write(str(Score))
    print(f"Your score is {Score} and you made a new Hi-Score.\nPrevious Hi-Score was {HighScore}.")



