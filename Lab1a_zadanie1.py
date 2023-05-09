import math 

a = int(input("Podaj wartość a: "))
b = int(input("Podaj wartość b: "))
c = int(input("Podaj wartość c: "))
while a==0:
    a = int(input("Podaj poprawną wartość a: "))

d = (b**2)+(-4*a*c)
if d>0:
    if d==0:
        x = (-1*b)/(2*a)
        print(x)
    else:
        x1 = ((-1*b)-math.sqrt(d))/(2*a)
        x2 = ((-1*b)+math.sqrt(d))/(2*a)
        print(x1, x2)
else:
    print("Brak rozwiązań")