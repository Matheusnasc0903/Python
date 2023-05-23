dviagem = float(input('Qual a distância em Km? '))
if dviagem <= 50:
    p = dviagem * 0.8
    print(f'O preço da viagem é de R${p:.2f}')
else:
    p = dviagem * 0.6
    print(f'O preço da viagem é de R${p:.2f}')
print('Tenha um Bom Dia!')
