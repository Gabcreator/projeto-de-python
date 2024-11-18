# Escreva um programa que some todos os números de 1 a 20 e exiba o resultado final.

import os 
os.system('cls')

soma =  0

for x in range(1, 20):
    
    soma += x

print(f'o resultado foi {soma}')