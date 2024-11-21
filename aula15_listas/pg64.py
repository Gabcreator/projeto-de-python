import os

os.system('cls')

lista_numeros = []

for i in range(3):
    numero = int (input('digite um número: '))

    lista_numeros.append(numero)

print(f'Lista gerada: {lista_numeros}')

print('-'*70)
numero_verificar = int(input('número para busca: '))
print('='*70)

if numero_verificar in lista_numeros:
    print(f'O número {numero_verificar} está na lista!')
else:
    print(f'O número {numero_verificar} não está na lista!')