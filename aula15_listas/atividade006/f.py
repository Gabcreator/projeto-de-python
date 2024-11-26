# Faça um programa que leia 5 nomes, depois imprima estes nomes com seus respectivos índices.
import os
os.system('cls')
lista = []

for nome in range(1, 6):
    nome = str(input('Digite um nome: '))
    lista.append(nome)
    print(lista)

indice_nome = input('Digite o nome de alguem desta lista: ')

if indice_nome in lista:
    indice = lista.index(indice_nome)
    print(f'o nome {indice_nome} está no índice {indice}')
else:
    print(f'o nome {indice_nome} não foi encontrado na lista !')

