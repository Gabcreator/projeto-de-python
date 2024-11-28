import os

os.system('cls')

lista = []
print(f'{lista}')

for lista_n in range (1, 11):
    item = input('digite o primeiro ítem na lista: ')
    lista.append(item)
    print(f'você adicionou o ítem {item} em sua lista (se não tiver nada para colocar aperte enter): {lista}')
print(f'sua lista completa foi: {lista}')