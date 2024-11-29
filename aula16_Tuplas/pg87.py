import os

os.system('cls')

nomes = ['Ágata', 'Bia', 'Coly', 'Isis']

for indice, nome in enumerate(nomes):
    minha_tupla = (indice, nomes)

    print(f"o nome '{minha_tupla[1]}', posição {minha_tupla[0]} da lista")
    print(f"O nome '{nome}', posição {indice} da lista. ")
    print('-'*70)