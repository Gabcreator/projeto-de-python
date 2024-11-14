# Faça um programa que some a quantidade de números pares encontrados no intervalo entre 0 e 100.
import os 


os.system('cls')

soma = 0

for par in range (1, 101):
    
    if( par % 2 == 0):
        soma += par
        print(par,end= "|")
print(f'a soma é {soma}')