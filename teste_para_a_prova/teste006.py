# Peça ao usuário um número inteiro e mostre a tabuada desse número (de 1 a 10) usando um for.

import os

os.system('cls')

numero = int(input('coloque um número: '))
valor = 0

for a in range(1, 11):
    valor = numero * a
    print(f'{numero} x {a} = {valor}')