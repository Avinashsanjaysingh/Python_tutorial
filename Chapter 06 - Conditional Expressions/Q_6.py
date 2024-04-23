'''
Write a program to calculate the grade of a student from his marks from the following scheme:
        90 - 100 -> Ex
        80 - 90 -> A 
        70 - 80 -> B 
        60 - 70 -> C 
        50 - 60 -> D 
        <50 -> F 
'''



a = int(input("Enter your percentage: "))

if ((a > 90) and (a <= 100)):
    print("Excellent")
elif ((a > 80) and (a <= 90)):
    print("A")
elif ((a > 70) and (a <= 80)):
    print("B")
elif ((a > 60) and (a <= 70)):
    print("C")
elif ((a >= 50) and (a <= 60)):
    print("D")
elif ((a >= 0) and (a < 50)):
    print("F")



