def dwojk(i, j, wynik):
    if i>1:
        wynik, i = wynik+((i%2)*j), int(i/2)
        return dwojk(i, j*10, wynik)
    elif i == 1:
        return wynik+j

a = int(input("Podaj wartość do zamiany na liczbę binarną:"))
print(dwojk(a, 1, 0))