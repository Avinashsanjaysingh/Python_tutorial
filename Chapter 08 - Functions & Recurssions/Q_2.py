# Write a python program using function to convert celsius to fahrenheit.

# F=(9/5)C+32

def celciusToFahrenheit(celcius):
    return ((celcius*9)/5)+32


print("Convert the temperature from celcius to fahrenheit.")

celcius = int(input("Enter the temperature in °C : "))

fahrenheit = celciusToFahrenheit(celcius)

print(f"{celcius}°C is {fahrenheit}°F.")



