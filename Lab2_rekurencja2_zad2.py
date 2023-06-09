def wynik(i):
    if i<3:
        return 1
    else:
        if i%2 == 0:
            print("f2")
            return wynik(i-3) + wynik(i-1) + 1
        else:
            print("f1")
            return wynik(i-1)%7
        
print(wynik(8))