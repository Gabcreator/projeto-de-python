# Crie uma lista com 5 números inteiros. Depois imprima a soma desses valores.
import os

os.system('cls')
soma = 0
for indice in range (1,6):
    numero = int(input('Digite um número: '))
    soma += numero


print(f"Todos os seus números inteiros somados juntos foi: {soma}")