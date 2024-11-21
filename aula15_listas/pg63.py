import os

os.system('cls')

print('-'*70)
print('ESTRUTURA DE DADOS: LISTAS[]')
print('='*70)

lista_mista = ['a', 'b', 3, 'John', 'e', 500, 'g', 'h']

lista1 = lista_mista[0]
lista2 = lista_mista[0:]
lista3 = lista_mista[0:6]
lista4 = lista_mista[0:6:2]
lista5 = lista_mista[::-1]

print(f'Fatiando uma lista: {lista1}')
print(f'Fatiando uma lista: {lista2}')
print(f'Fatiando uma lista: {lista3}')
print(f'Fatiando uma lista: {lista4}')
print(f'Fatiando uma lista: {lista5}')

print('-'*70)
print('Fim do programa')
print('='*70)