import os

os.system('cls')

print('-'*70)
print('ESTRUTURAS DE DADOS LISTAS []')
print('-'*70)

inteiros = [1, 2, 3, 4]
vogais = ['a', 'e', 'i', 'o', 'u']
nomes = ['jane', 'carol', 'john']
heterogenea = ['John', 80, 1.90, 'AB']
lista_lista = ['a', 'e', 'i', 'o', 'u',[1, 2, 3, 4]] 

print(f'Lista inteiros {inteiros}')
print(f'Lista de vogais {vogais}')
print(f'Lista de nomes {nomes}')
print(f'Lista misturada {heterogenea}')
print(f'Lista de lista {lista_lista}')

lista_indice0 = inteiros[0]
lista_vogais = vogais[1]
lista_nome = nomes[2]
lista_heterogenea = heterogenea[3]
lista_num_lista = lista_lista[1]

print('-'*70)
print('Acessando os elementos de uma lista')
print('='*70)
print(f'Lista de números: {lista_indice0}')
print(f'Lista de vogais: {lista_vogais}')
print(f'Lista de nomes: {lista_nome}')
print(f'Lista heterogêmea: {lista_heterogenea}')
print(f'Lista de Lista: {lista_num_lista}')

print('-'*70)
print('FIM DO PROGRAMA')
print('-'*70)