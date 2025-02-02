A, B = map(int, input().split())

A = int(A)
B = int(B)

if (B<A):
    hora_de_jogo = (24 - A) + B
    
elif(B>A):
    hora_de_jogo = B - A

else:
    hora_de_jogo = 24
    
print(f'O JOGO DUROU {hora_de_jogo} HORA(S)')