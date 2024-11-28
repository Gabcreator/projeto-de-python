import os

os.system('cls')

lista = ['xicara', 'mala', 'panela', 'celular', 'computador']
print(f'{lista}')

for lista_n in range (1, 10):
    lista.append(lista_n)
    lista_n = input('digite um ítem na lista: ')
    print(f'você adicionou o ítem {lista_n} em sua lista: {lista}')