import math
n = pow(2, 11)
for i in range (n):
    probability = 1 - pow((n-1)/n, i)
    if(probability >= 0.5):
        print(i)
        break