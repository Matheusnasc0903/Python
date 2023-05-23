print(50*'-')
print('Calculo de Aumento Salárial')
print(50*'-')
sal = float(input('Informe o seu salário em R$'))
if sal > 1500:
    sal = sal + sal/100*10
else:
    sal = sal + sal/100*15
print(f'Seu novo salário é de R${sal}')
