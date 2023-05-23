frase = 'Meu nome é Matheus'
print(frase)
#ANÁLISE
print('A frase contém', len(frase), 'caracteres')
print('Temos', frase.count('e'), 'letras "e"')
print('A palavra "nome" inicia na posição', frase.find('nome'))
print('Dentro da frase tem a palavra "Meu"?', 'Meu' in frase)
#FATIAMENTO
print(frase[11:])
print(frase[11:18])
print(frase[::2])
print(frase[:4])
#TRANSFORMAÇÃO
print(frase.replace('Matheus', 'João'))
print('Tudo em Maiúsculas', frase.upper())
print('Tudo em Minúsculas', frase.lower())
print('Capitalizado', frase.capitalize())
print('Inicio das palavras em maiúsculas', frase.title())
#.strip .rstrip .lstrip usados para tirar espaços no inicio e final
print(frase.strip())
#DIVISÃO
print(frase.split())
div = frase.split()
print(div[1])
print(div[1][2])
#JUNÇÃO
