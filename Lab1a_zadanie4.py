import random

n = random.randint(5,15)
tab = []

for i in range(n):
    tab.append(random.randint(1,20))

minValue=tab[0]

for i in range(1,len(tab)):
    if minValue>tab[i]:
        minValue = tab[i]
print(minValue)
print(tab)