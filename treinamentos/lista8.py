import os

os.system('cls')

lista = []

for l in range (1, 11):
    itens = input('Digite um ítem para colocar na lista: ')
    lista.append(itens)
    print(lista)

remover = input('Digite um ítem para remover: ')
deletar = lista.index(remover)
lista.pop(deletar)

print(lista)