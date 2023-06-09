# Wersja 1

a = int(input("Podaj wartość a: "))
b = int(input("Podaj wartość b: "))

while a != b:
    if a>b: a = a - b
    else: b = b - a

print(a)

# Wersja 2

def NWD(a,b):
    a, b = b, a % b
    if a!=0 and b!= 0:
        return NWD(a,b)
    elif a == 0:
        return b
    elif b == 0:
        return a

x = int(input("Podaj pierwszą wartość: "))
y = int(input("Podaj drugą wartość: "))
print(NWD(x,y))