import os

os.system('cls')

entrada = input("Digite números separados por espaço: ")

numeros_str = entrada.split()

numeros = []
for num_str in numeros_str:
    numeros.append(int(num_str))

escolha = input("Deseja criar uma cópia? (s/n): ").strip().lower()

if escolha == 's':
    lista_copiada = numeros.copy()
    print(f"Copia da lista: {lista_copiada}")
else:
    print("A lista não foi copiada.")

print(f"Lista fornecida: {numeros}")