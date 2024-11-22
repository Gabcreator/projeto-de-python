import os

os.system('cls')

entrada = input('Digite números separados por espaço: ')

numeros_str = entrada.split()

numeros = []
for num_str in numeros_str:
    numeros.append(int(num_str))

ordem = input("Digite 'asc' para a ordem acressente ou 'desc'"
"para ordem decressente: ").strip().lower()

if ordem == 'asc':
    numeros.sort()
    print(f"Lista ordenada ordem ascendente: {numeros}")
elif ordem == 'desc':
    numeros.sort(reverse=True)
    print(f"Lista ordenada em ordem descendente: {numeros}")
else:
    print("opcão inválida! a lista não foi ordenada.")

print("lista fornecida", numeros)