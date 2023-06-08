def silnia(n):
    if n == 0: return 1
    elif n>=1:
        Silnia = [1]
        i = 1
        while i<=n:
            Silnia.append(Silnia[i-1]*i)
            i+=1
        return Silnia[i-1]
    
n = int(input("Podaj n: "))
if (n>=0): print(silnia(n))
else: print("Podano niepoprawny argument")
            