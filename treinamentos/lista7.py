import os

os.system('cls')

lista = ['copo', 'celular', 'computador']
print(f'{lista}')

for itens in range(1, 3):
    itens = input('Digite um ítem pata colocar na lista: ')
    print(f'o item {itens} foi adicionado na sua lista: {lista}')