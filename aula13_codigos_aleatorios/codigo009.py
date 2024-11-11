#o seu cliente quer que você crie um programa que coloque uma frase separada 
import os
os.system('cls')

frase = str(input('coloque uma frase: '))

frase_separada = frase.split()

print(f'a sua frase separada ficou{frase_separada}')