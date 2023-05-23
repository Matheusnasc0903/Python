from math import hypot
co = float(input('Cateto Oposto: '))
ca = float(input('Cateto Adjacente: '))
h = hypot(co, ca)
# h = (co**2+ca**2) ** (1/2)
print(f'A hipotenusa mede {h:.2f}')
