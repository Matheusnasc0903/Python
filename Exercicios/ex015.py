d = int(input('Por quantos dias o carro foi alugado:'))
km = float(input('Quantos Km foram rodados:'))
p = d*60 + km*0.15
print(f'O valor do aluguel é de R${p:.2f}')
