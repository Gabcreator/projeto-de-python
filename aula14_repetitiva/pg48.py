import os

os.system('cls')

print('-'*70)
print('ESTRUTURA DE CONTROLE FOR RANGE')
print('-'*70)

for var_interadora in range(1, 7):
    print(f'valor: {var_interadora}', end=" | ")

print()
print()

inicio = 1
fim = 7 
passo = 2

for var_interadora in range(inicio, fim, passo):

    print(f'Valor: {var_interadora}', end=" | ")

print()
print()