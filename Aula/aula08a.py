from math import sqrt
from random import randint
import emoji

n = float(input('Digite um número: '))
print(f'A raiz de {n} é {sqrt(n):.2f}')
print(f'Este é um número aleatório gerado pelo Python: {randint(1, 10)}')
print(emoji.emojize('Python é :polegar_para_cima:', language='pt'))
