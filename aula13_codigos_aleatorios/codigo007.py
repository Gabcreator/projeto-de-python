#faça um programa que o seu cliente coloque uma frase e depois coloque quantas palavras tem nesta frase
import os
os.system('cls')

frase = str(input('coloque uma frase: '))

tamanho_da_frase = len(frase)

print(f'Esta frase tem {tamanho_da_frase} caracteres')