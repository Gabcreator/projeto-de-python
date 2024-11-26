# Faça um programa que preencha uma lista com 50 números aleatórios. Depois fatie essa lista em 5 listas de 10 elementos.
import os
import random
os.system('cls')

lista = []

for i in range (0, 50):
    numeros = random.randint(0,50)
    lista.append(numeros)
print(f'sua lista aleatória foi: {lista}')