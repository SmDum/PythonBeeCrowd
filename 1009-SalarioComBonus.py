nome = str(input())
salario = float(input())
vendas = float(input())

valor = salario + (0.15 * vendas)

print(f'TOTAL = R$ {valor:.2f}')