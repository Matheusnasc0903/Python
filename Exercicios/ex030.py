from math import trunc
n = trunc(float(input('Digite um número: ')))
poi = n % 2
if poi == 0:
    print(f'O número {n} é PAR')
else:
    print(f'O número {n} é IMPAR')
