nome = input('Nome completo: ').strip()
nomed = nome.split()
print(f'''Seu nome com todas as letras MAIÚSCULAS: {nome.upper()}
Seu nome com todas as letras minúsculas: {nome.lower()}
Seu nome completo tem {len(nome)-nome.count(" ")} letras
Seu 1º nome tem {len(nomed[0])} letras ''')
