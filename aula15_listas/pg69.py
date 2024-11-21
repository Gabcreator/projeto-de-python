import os

os.system('cls')

entrada = input('Digite números separados por espaço: ')

numeros_str = entrada.split()

numeros = []
for num_str in numeros_str:
    numeros.append(int(num_str))

busca_numero = int(input('Digite o número que deseja encontrar: '))

if busca_numero in numeros:
    indice = numeros.index(busca_numero)
    print(f'O número {busca_numero} está no índice {indice}.')
else:
    print(f'o número {busca_numero} não se encontra na lista')

print(f'Lista fornecida: {numeros}')