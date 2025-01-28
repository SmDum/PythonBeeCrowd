from math import sqrt

valor1, valor2 = input().split()
valor1 = float(valor1)
valor2 = float(valor2)

valor3, valor4 = input().split()
valor3 = float(valor3)
valor4 = float(valor4)

total = sqrt((valor3-valor1)**2 + (valor4-valor2)**2)

print(f'{total:.4f}')