from math import sqrt

p1 = 164 / 15550

p2 = 228 / 15550

n1 = 164

n2 = 228

N1 = 15550

N2 = N1

p =  (n1 * p1 + n2 * p2) / (n1 + n2)

Z = (p1 - p2) / ((p * (1 - p) * (1/N1 + 1/N2))**0.5)
print(Z)