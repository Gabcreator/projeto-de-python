import os 

os.system('cls')

print('-'*70)
print('ESTRUTURA DE CONTROLE SOMATÓRIO')

print()

soma = 0

for var_interadora in range(0, 4):
    numero = int(input(f'Digite o {var_interadora + 1}º número: '))

    soma += numero

print('-'*50)
print(f'a soma dos números é: {soma}')
print('-'*50)
print()