# Crie a lista [1, 2, 3, 5, 6] e depois insira o valor que está faltando na posição correta.
import os

os.system('cls')

lista = [1, 2, 3, 5, 6]
print(f'{lista}')

posição = int(input('Digite a posição onde você quer colocar o número faltando: '))
elemento = input('Digite o número faltando: ')

if posição >= 0 and posição <= len(lista):
    lista.insert(posição, elemento)
    print("Lista após a inserção:", lista)
else:
    print(f"posição fora do intervalo 0, {len(lista)}")