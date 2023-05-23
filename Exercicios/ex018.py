from math import cos, tan, sin, radians
angulo = float(input('Digite o ângulo: '))
seno = sin(radians(angulo))
cosseno = cos(radians(angulo))
tangente = tan(radians(angulo))
print(f'O ângulo de {angulo} tem o Seno de {seno:.2f}, o Cosseno de {cosseno:.2f} e a Tangente de {tangente:.2f}')
