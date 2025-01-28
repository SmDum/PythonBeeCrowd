def maiorAB(a, b):
    return (a + b + abs(a - b)) // 2

a, b, c = map(int, input().split())

maior = maiorAB(maiorAB(a, b), c)

print(f"{maior} eh o maior")
