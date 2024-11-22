import os

os.system('cls')

print('-'*70)
print('VARRENDO LISTAS DENTRO DE LISTAS')
print('='*70)

jogo_da_velha = [
                ['X' , 'O', 'X'],
                ['X' , 'O', 'X'],
                ['X' , 'O', 'X']
]

print(jogo_da_velha)
print()

print(f'Na Linha 1 Coluna 1, Existe um: {jogo_da_velha[1][1]}')
print(f'Na Linha 0 Coluna 2, existe um: {jogo_da_velha[0][2]}')

print()

for linha in range(0, len(jogo_da_velha)):
    for coluna in range(0, len(jogo_da_velha)):
        print(jogo_da_velha[linha][coluna], end=' ')
    print()
print()