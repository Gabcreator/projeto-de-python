# Faça um programa que calcule os números primos em um intervalo pré-determinado pelo usuário.
import os
os.system('cls')

numero = int(input('coloque um número: '))
numero2 = int(input('coloque o segundo número: '))
for principal in range (numero + numero2):
    print(f'os primos vão ser {principal}')