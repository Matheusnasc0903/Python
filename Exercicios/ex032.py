from datetime import date
print(50*'*')
print(12*" ", 'Analizando Anos Bissextos')
print(50*'*')

ano = int(input('Qual Ano Alalizar (Para o ano atual digite "0"): '))

print(50*'-')
if ano == 0:
    ano = date.today().year
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print(f'O ano de {ano} é Bissexto')
else:
    print(f'O ano de {ano} não é Bissexto')
print(50*'-')
