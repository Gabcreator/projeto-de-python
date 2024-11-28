# aceite números até o usuário apertar 's' mostre a lista inversa quantos números tem na lista o número maior e o número menor
import os

os.system('cls')

lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

numero = input('Digite um número: ')
while (numero != 's'):
    lista.append(float(numero))
    numero = input('Digite um número: ')
    