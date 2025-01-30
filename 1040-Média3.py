N1, N2, N3, N4 = input().split()

N1 = float(N1)
N2 = float(N2)
N3 = float(N3)
N4 = float(N4)

media = ((N1*2)+(N2*3)+(N3*4)+N4)/10
print(f'Media: {media:.1f}')

if media > 7:
    print('Aluno aprovado.')
elif media < 5:
    print('Aluno reprovado.')
else:
    print('Aluno em exame.')
    
    NE = float(input())
    print(f'Nota do exame: {NE:.1f}')
    
    media = (media+NE)/2
    
    print('Aluno aprovado.' if media>5 else 'Aluno reprovado.')
    
    print(f'Media final: {media:.1f}')