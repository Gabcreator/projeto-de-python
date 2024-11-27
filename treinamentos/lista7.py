import os

os.system('cls')

lista = []
print(f'{lista}')

for itens in range(1, 11):
    lista.append(itens)
    itens = input('Digite um ítem pata colocar na lista: ')
    print(f'o item {itens} foi adicionado na sua lista: {lista}')