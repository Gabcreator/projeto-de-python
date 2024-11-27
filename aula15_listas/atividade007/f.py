# Faça um programa que gere 10 números aleatórios. Após gerar esses números, crie duas listas novas com ordenação ascendente e descendente.
import os 
import random
os.system('cls')

lista = []
lista_c = []
lista_m = []

for i in range (1, 10):
    lista1 = random.randint(1, 1000)
    lista.append(lista1)
    lista_c.append(lista1)

    lista_m.append(lista1)
lista_c.sort()
lista_m.sort(reverse=True)

print(f'A sua lista crescente com números aleatórios é: {lista_c}')
print(f'A sua lista decrescente com números aleatórios é: {lista_m}')