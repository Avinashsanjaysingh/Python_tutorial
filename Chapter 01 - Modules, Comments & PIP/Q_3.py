#Install an external module and use it to perform an operation of your interest.

# "pip install pyttsx3" (text to speech module in python)

import pyttsx3

# Create a text-to-speech engine
engine = pyttsx3.init()

# Enter the text you want to convert to speech
text_to_speak = "Hello, I'm using pyttsx3 to convert text into speech!"

# Set properties (optional)
engine.setProperty('rate', 150)  # Speed of speech

# Convert text to speech
engine.say(text_to_speak)

# Wait for the speech to finish
engine.runAndWait()


# python your_script.py
