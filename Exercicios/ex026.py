frase = str(input('Digite uma frase: ')).strip()
print(f'A frase tem {frase.lower().count("a")} letra(s) "A"')
print(f'A primeira está na posição {frase.lower().find("a")+1}')
print(f'A última está na posição {frase.lower().rfind("a")+1}')
