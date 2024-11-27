# Faça um programa que receba 7 números inteiros. Depois quebre essa lista em: lista de pares e lista de ímpares. 
import os
os.system('cls')

lista_par = []
lista_impar = []

for i in range (1, 8):
    numeros = int(input('Digite um número: '))
    if numeros % 2 == 0:
        print('O número é par: ')
        lista_par.append(numeros)
        
    else:
        print('o número é ímpar')
        lista_impar.append(numeros)

print(f'A sua lista de números ímpares: {lista_impar}')
print(f'A sua lista de números pares é: {lista_par}')