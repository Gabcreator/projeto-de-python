import os

os.system('cls')

entrada = input("Digite números separados por espaço: ")

numeros_str = entrada.split()

numeros = []
for num_str in numeros_str:
    numeros.append(int(num_str))

escolha = input("Deseja limpar esta lista? (s/n): ").strip().lower()

print(f"A lista original é {numeros}")

if escolha == 's':
    numeros.clear()
    print(f"Lista limpa: {numeros}")
else:
    print("A lista não foi limpa.")

