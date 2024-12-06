import os
os.system('cls')

print('-'*70)
print('ESTRUTURA DE DADOS: DICIONARIOS')
print('-'*70)

compras = {}
pessoas = {}
cores = {}
elementos = dict()
numeros = dict()

compras['id'] = 1
compras['item'] = 'caderno'
compras['valor'] = 10.80

pessoas['id'] = '0010'
pessoas['nome'] = 'Sherlok Homes'
pessoas['endereço'] = 'Barker Street'
pessoas['numero'] = '221B'
pessoas['cidade'] = 'Londres'
pessoas['pais'] = 'Inglaterra'

cores['red'] = 'vermelho'
cores['green'] = 'verde'
cores['blue'] = 'azul'

elementos['Pb'] = 'Chumbo'
elementos['Au'] = 'ouro'
elementos['N'] = 'Nitrogênio'

numeros[1] = 100
numeros[2] = 200
numeros[3] = 300

print(f'Minhas compras: {compras}')
print(f'Detetives: {pessoas}')
print(f'cor RBG: {cores}')
print(f'Tabela periódica: {elementos}')
print(f'Listagem de números: {numeros}')
print()
print('-'*100)