vel = float(input('Qual a sua velocidade em Km/h? '))
lv = int(input('Qual a velocidade máxima da pista em Km/h? '))
if vel > lv:
    acima = vel-lv
    multa = acima * 7
    print(f'Você passou o limite de velocidade em {acima:.2f} Km/h')
    print(f'A multa é de R${multa:.2f}')
else:
    print('Você está dentro do limite de velocidade permitida!')