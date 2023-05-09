while True:
    n = int(input("Wprowadź długość ciągu liczb: "))
    if n>0:
        break
ile = 0
for i in range(n):
    a = int(input("Wprowadź kolejną liczbę ciągu: "))
    if a<0:
        ile+=1
print(ile)