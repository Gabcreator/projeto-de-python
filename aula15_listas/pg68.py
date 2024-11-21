import os

os.system('cls')

entrada = input('Digite números separados por espaço: ')

numeros_str = entrada.split()

numeros = []
for num_str in numeros_str:
    numeros.append(int(num_str))

numero_para_contar = int(input('Digite o número que deseja contar: '))

contagem = numeros.count(numero_para_contar)

if contagem > 0:
    print(f'o número {numero_para_contar} apareçe em {contagem} vezes na lista!')
else:
    print(f'O número {numero_para_contar} não apareçe na lista.')

print(f'Lista fornecida: {numeros}')