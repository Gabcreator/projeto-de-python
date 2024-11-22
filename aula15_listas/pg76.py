import os

os.system('cls')

print('-'*70)
print('SAÍDA COM FOR... ENUMERATE()')
print('='*70)

soma = 0

lista_numeros = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

for indice, numero in enumerate(lista_numeros):
    soma += numero
    print(f'indice: {indice} = numero: {numero}')

print('-'*70)
print(f'A soma de todos os números é: {soma}')
print('Fim do programa')
print('-'*70)