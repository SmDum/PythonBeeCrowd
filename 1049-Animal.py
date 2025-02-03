A = input()
B = input()
C = input()

if A == 'vertebrado':
    if B == 'ave':
        if C == 'carnivoro':
            print('aguia')
        else:
            print('pomba')
    else:  # mamifero
        if C == 'onivoro':
            print('homem')
        else:
            print('vaca')
else:  # invertebrado
    if B == 'inseto':
        if C == 'hematofago':
            print('pulga')
        else:
            print('lagarta')
    else:  # anelideo
        if C == 'hematofago':
            print('sanguessuga')
        else:
            print('minhoca')
