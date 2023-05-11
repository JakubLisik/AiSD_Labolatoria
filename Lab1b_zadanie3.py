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
        print(lenght_check)
        print(b[k],a[k])
        while lenght_check>=0: 
            lenght_check -= 1
            if b[k] > a[k]:  #Coś tu nie działa nwm dlaczego, psycha siedzi...
                tab[j] = a
                tab[x] = b
                print(tab, a, b)
                break
            k += 1
        j -= 1
        x -= 1
print(tab)