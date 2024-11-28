import os

os.system('cls')

lista = []

for a in range (1, 20):
    desejos = input('Digite seus desejos: ')
    lista.append(desejos)
    print(f'seu desejo {desejos} foi adicionado na lista {lista}')