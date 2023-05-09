import math
uk1 = 1
uk2 = 1

print('Digite um valor de K: ')
k = int(input())

ms5 = math.sqrt(5)
ukform = int(((1 + ms5)/(2 * ms5)) * (((1 + ms5)/2)**k) + ((ms5 - 1)/(2 * ms5)) * (((1-ms5)/2)**k))

k1 = k+1

for i in range (k1):
    if i <= 1: 
        uk = 1
    else:
        uk = uk1 + uk2
    print("k = ", i, "      u(", i, ") = ", uk)
    uk2 = uk1
    uk1 = uk

print("\nPela Fórmula temos que o último número é: ", ukform, "\n")

