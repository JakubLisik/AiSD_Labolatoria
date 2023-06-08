def list(n):
    if n == 0: return 1
    elif n == 1: return 1
    elif n>1:
        List = [1,1]
        i = 2
        while (i<=n):
            List.append(2*List[i-1]-List[i-2])
            i+=1

        return List[i-1]
    
n = int(input("Podaj n: "))
if (n>=0): print(list(n))
else: print("Podano niewłaściwy argument")