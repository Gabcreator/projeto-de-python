# Faça um programa que sorteia os números da Mega Sena e da Lotofácil
import os
import random
os.system('cls')
lista = []
lista2 = []

for i in range (1, 7):
    sorteado = random.randint(1, 60)
    lista.append(sorteado)
for o in range (1, 16):
    sorteado_s = random.randint(1, 25)
    lista2.append(sorteado_s)

print(lista)
print(lista2)