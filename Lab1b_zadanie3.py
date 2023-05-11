values = input("Wprowadź wartości do tablicy: ")

tab = values.split()

for i in range(1, len(tab)):
    a = str(tab[i])
    j = i-1
    x = i
    while j>=0:
        b = str(tab[j])
        if len(a)>len(b):
            lenght_check = len(b)
        else:
            lenght_check = len(a)
        k = 0
        for k in range(lenght_check):
            if int(b[k]) > int(a[k]):
                tab[j] = a
                tab[x] = b
                print(tab, a, b, x, j, k)
                break
            elif int(b[k]) < int(a[k]):
                break
        j -= 1
        x -= 1
print(tab)