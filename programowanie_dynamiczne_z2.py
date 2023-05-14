
def wyznacz(i,j):
    Tab = [[0] * (j+1) for z in range(i+1)]
    Tab[0][0] = -1

    for x in range(i+1):
        for y in range(j+1):
            if x > 0 and y == 0:
                Tab[x][y] = 0
            elif x == 0 and y > 0:
                Tab[x][y] = 1
            elif x>0 and y>0:
                Tab[x][y] = (Tab[x-1][y]+Tab[x][y-1])/2

for row in Tab:
    print('    '.join([str(elem) for elem in row]))

print("\n")

#Do poprawy