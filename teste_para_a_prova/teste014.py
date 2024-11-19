import os

os.system('cls')

numero = int(input('coloque um número: '))
resultado = 0

for a in range (1, 21):
    resultado = numero * a
    print(f'{numero} x {a} = {resultado}')