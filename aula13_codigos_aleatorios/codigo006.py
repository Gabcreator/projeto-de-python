#Faça um programa que receba uma frase e, em seguida, mostre quantas vezes as vogais foram utilizadas.
import os 

os.system('cls')

frase = str(input('coloque uma frase: '))

quantidade_caracteres_a = frase.count('a')
quantidade_caracteres_e = frase.count('e')
quantidade_caracteres_i = frase.count('i')
quantidade_caracteres_o = frase.count('o')
quantidade_caracteres_u = frase.count('u')

print(f'a sua frase tem {quantidade_caracteres_a} a')
print(f'a sua frase tem {quantidade_caracteres_e} e')
print(f'a sua frase tem {quantidade_caracteres_i} i')
print(f'a sua frase tem {quantidade_caracteres_o} o')
print(f'a sua frase tem {quantidade_caracteres_u} u')