# Dada uma lista de nomes, exiba cada nome acompanhado de sua posição na lista.

import os

os.system('cls')

for a in range (1, 4):
    nome = str(input('coloque o nome dos participantes: '))
    print(f'{a}-{nome}')