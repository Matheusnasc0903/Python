print(25*'-=')
a = float(input('1ª reta: '))
b = float(input('2ª reta: '))
c = float(input('3ª reta: '))
print(25*'-=')
if a+b > c and a+c > b and b+c > a:
    print('Estas retas \033[1;32;40mPODEM\033[m formar um triângulo')
else:
    print(f'Estas retas \033[1;31;40mNÃO PODEM\033[m formar um triângulo!')
