import math
n = pow(2, 11)
for i in range (n):
    probability = 1 - (math.factorial(n) / (math.factorial(n - i) * pow(n, i)))
    if(probability >= 0.75):
        print(i)
        break