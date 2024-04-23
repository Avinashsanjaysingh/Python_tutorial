# decimal to binary


x = int(input("Enter a number less than 7 digits: "))

while ((x < 0) and (x > 1048576)):
    print("Enter a number less than 7 digits.")
    x = int(input("Enter the number: "))

y = x

a = 0
b = 0
c = 0
d = 0
e = 0
f = 0
g = 0
h = 0
i = 0
j = 0
k = 0
l = 0
m = 0
n = 0
o = 0
p = 0
q = 0
r = 0
s = 0
t = 0


if x >= 524288:
    t = 1
    x %= 524288

if x >= 262144:
    s = 1
    x %= 262144

if x >= 131072:
    r = 1
    x %= 131072

if x >= 65536:
    q = 1
    x %= 65536



if x >= 32768:
    p = 1
    x %= 32768

if x >= 16384:
    o = 1
    x %= 16384

if x >= 8192:
    n = 1
    x %= 8192

if x >= 4096:
    m = 1
    x %= 4096



if x >= 2048:
    l = 1
    x %= 2048

if x >= 1024:
    k = 1
    x %= 1024

if x >= 512:
    j = 1
    x %= 512

if x >= 256:
    i = 1
    x %= 256



if x >= 128:
    h = 1
    x %= 128

if x >= 64:
    g = 1
    x %= 64
    
if x >= 32:
    f = 1
    x %= 32
        
if x >= 16:
    e = 1
    x %= 16



if x >= 8:
    d = 1
    x %= 8
                
if x >= 4:
    c = 1
    x %= 4
                    
if x >= 2:
    b = 1
    x %= 2
                        
if x >= 1:
    a = 1


a1 = str(d) + str(c) + str(b) + str(a)
a2 = str(h) + str(g) + str(f) + str(e)
a3 = str(l) + str(k) + str(j) + str(i)
a4 = str(p) + str(o) + str(n) + str(m)
a5 = str(t) + str(s) + str(r) + str(q)


if y < 16:
    print(a1)
elif y < 256:
    print(a2,a1)
elif y < 4096:
    print(a3,a2,a1)
elif y < 65536:
    print(a4,a3,a2,a1)
elif y < 1048576:
    print(a5,a4,a3,a2,a1)




