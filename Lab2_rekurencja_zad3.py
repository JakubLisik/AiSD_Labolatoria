def f(i):
    if i == 1: return 4
    else:
        return 1/(1 - f(i-1))
    
print(f(100))