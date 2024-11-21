import os

os.system('cls')

lista = [1, 2, 3, 4]

posição = int(input('Posição onde deseja inserir o evento: '))
elemento = input('Elemento a ser inserido: ')

if posição >= 0 and posição <= len (lista):

    lista.insert(posição, elemento)
    print("lista após a inserção:", lista)
else:
    print(f"Posição fora do intervalo 0, {len(lista)}")