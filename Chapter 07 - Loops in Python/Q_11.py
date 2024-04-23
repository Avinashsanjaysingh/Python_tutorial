'''
    n should always start n>=2
    Let say if user input is 2.(n=2)

    Output:-
    @
    @
    @**
      **@
        @
        @

    similarly if user input is 3.(n=3)
    Output:-
    @
    @
    @
    @***
       ***
         ***@
            @
            @
            @

    similarly if user input is 4.(n=4)
    Output:-
    @
    @
    @
    @
    @**** 
        **** 
           **** 
              ****@
                  @
                  @
                  @
                  @

'''

n = int(input("Enter the value of n: "))
while n < 2:
    print("n should be greater than or equal to 2.")
    n = int(input("Enter the value of n: "))


# creating first part
for i in range(0,n):
    print("@")
for j in range(0,n):
    if j == 0:
        print("@",end='')
    print("*",end='')
print()

# creating second part
for i in range(0,n-2):
    m = (n + (i * (n-1)))
    for j in range(0,m):
        print(" ",end='')
    print("*"*n)

# creating third part
m = (2 + ((n-2)*n))

for i in range(0,m):
    print(" ",end='')
for i in range(0,n):
    print("*",end='')
print("@")

for i in range(0,n):
    print(" "*(m+n-1),("@"))


