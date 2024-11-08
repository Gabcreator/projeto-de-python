#Faça um programa que leia uma frase e depois exiba na tela:
# A frase em minúsculas, a frase em maiúsculas, a quantidade de caracteres na frase e quantas letras tem a 2ª palavra na frase.

import os
os.system("Cls")

texto = str(input('coloque um texto: '))

maiusculo = texto.upper()
minusculo = texto.lower()

quantidade = len(texto)
lista = texto.split()

segunda_palavra = len(lista[1])

print('-'*40)
print(f'o seu texto tem {maiusculo}')
print(f'o seu texto tem {minusculo}')
print(f'o seu texto tem {quantidade} carácteres')
print(f'o seu texto tem {lista}')
print(f'a sua segunda palavra tem {segunda_palavra} carácteres')