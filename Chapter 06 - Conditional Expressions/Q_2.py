# Write a program to find out whether a student is pass or fail, if it requires total 40% and at least 33% in each subject to pass. Assume 3 subjects and take marks as an input from the user.


'''
# It only takes marks for three questions as said in the problem.

a = int(input("Enter the marks of Maths: "))
b = int(input("Enter the marks of Science: "))
c = int(input("Enter the marks of Arts: "))

d = int((a+b+c)/3)

if a < 33:
    print("You failed in Maths.")
if b < 33:
    print("You failed in Science.")
if c < 33:
    print("You failed in Arts.")
if d < 40:
    print("You could not get overall passing marks.")

if (((a >= 33) and (b >= 33)) and ((c >= 33) and (d >= 40))):
    print("You passed.")
'''

# It takes as much subjects as you want to feed.

a = int(input("\nEnter the number of subjects: "))
while a <= 0:
    a = int(input("Enter the number of subjects: "))

b = []

for i in range(0,a):
    print("Enter the marks of the subject",i+1,":",end=' ')
    j = int(input(""))
    while ((j <= 0) or (j >= 100)):
        j = int(input("Enter the marks between 0 and 100: "))
    b.append(j)

c = 0

for k in range(0,33):
    if k in b:
        c += 1

d = 0
for l in range(0,a):
    d += b[l]
e = int(d/a)

if c > 0:
    print("You Failed!")
elif d < 40 :
    print("You Failed!")
else:
    print("You Passed!")



