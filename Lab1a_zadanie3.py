import random

n = random.randint(3,9)
tab = []

for i in range(n):
    tab.append(random.randint(1,20))

x = int(input("Podaj wartość do znalezienia (1-20): "))

for i in range(len(tab)):
    if x==tab[i]:
        print("Ta liczba znajduje się w tablicy")
        break
    elif i==len(tab)-1:
        print("Tej liczby nie ma w tablicy")
        
print(tab)