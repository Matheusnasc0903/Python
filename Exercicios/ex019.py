from random import choice
n1 = input('1º aluno: ')
n2 = input('2º aluno: ')
n3 = input('3º aluno: ')
n4 = input('4º aluno: ')
n5 = input('5º aluno: ')
lista = [n1, n2, n3, n4, n5]
escolhido = choice(lista)
print(f'O escolhido foi {escolhido}')
