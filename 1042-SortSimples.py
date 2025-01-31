N1, N2, N3 = map(int, input().split())

original = [N1, N2, N3]

ordenado = sorted(original)

for item in ordenado:
    print(item)

print()

for item in original:
    print(item)