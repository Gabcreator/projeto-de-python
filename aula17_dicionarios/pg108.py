import os

os.system('cls')

elementos = {}
periodica = []

for c in range(2):
    print(f"Entrada de dados {c + 1}")
    simbolo = str(input('Símbolo do elemento: '))
    nome = str(input('Nome do elemento: '))

    elementos['simbolo'] = simbolo
    elementos['nome'] = nome

    periodica.append(elementos.copy())

print()
print('-'*70)
print("Elementos da tabela periódica: ")
print(periodica)
print('-'*70)
print()

print("Detalhes dos elementos:")
for elemento in periodica:
    for chave, valor in elementos.items():
        print(f'{chave.captalize()}: {valor}')
    print('-'*70)
    