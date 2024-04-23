'''
    Write a program to fill in a letter template given below with name and date.
                letter = "Dear <|NAME|>
                            Yoy are selected!
                            <|Date|>"
'''

from datetime import datetime

date = datetime.now().strftime("%d-%m-%Y")

name = input("Enter your name: ")

print("\nDear", name, "\n You are selected!\n  ", date)

