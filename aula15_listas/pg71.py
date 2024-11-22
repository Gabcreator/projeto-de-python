import os

os.system('cls')

lista = [1, 2, 3, 4]

print("Lista original:", lista)

elemento = input('elemento a ser removido: ')

if elemento.isdigit():
    elemento = int(elemento)
if elemento in lista:
    lista.remove(elemento)
    print(f"lista após a remoção:", lista)
else:
    print("Elemento não encontrado na lista.")