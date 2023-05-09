import random

n = random.randint(5,8)
m = random.randint(2,3)
tab = [[]]

for j in range(m):
    tab.append([])

for j in range(m+1):
    for i in range(n):
        tab[j].append(random.randint(1,20))

print(tab)

for j in range(m+1):
    a = tab[j][0]
    x = j
    y = 0
    minValue = tab[j][0]
    for i in range(1,n):
        if minValue>tab[j][i]:
            minValue = tab[j][i]
            y = i
    tab[j][0] = minValue
    tab[x][y] = a
    print(minValue)
    print(tab[j])