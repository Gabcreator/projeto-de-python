#o seu cliente quer que você crie um sistema que tire a primeira e a utima palavra da frase
import os
os.system('cls')

frase = str(input('coloque uma frase: '))

frase_sem_primeira_palavra_e_nem_a_utima = frase.strip(' ')

print(f'a sua frase sem o começo e nem o fim ficou: {frase_sem_primeira_palavra_e_nem_a_utima}')