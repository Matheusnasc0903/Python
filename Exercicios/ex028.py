from random import randint, choice
n = randint(0, 5)
f = ['Errou touxa', 'Tente de novo', 'Errado', 'Não foi esse']
nu = int(input('Qual número de 0 a 5 estou pensando? '))
if nu < 0 or nu > 5:
    print('Não sabe ler?')
elif nu == n:
    print('Você acertou!')
else:
    print(f'{choice(f)}! Pensei no {n}')
print('Obrigado por brincar...')
