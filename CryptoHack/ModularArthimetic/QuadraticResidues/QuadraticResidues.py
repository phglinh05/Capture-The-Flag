p = 29
ints = [14,6,11]
t = 0
for i in range(0, 3):
    for j in range(1, p):
        if(j*j % 29 == ints[i]):
            print(j)
        