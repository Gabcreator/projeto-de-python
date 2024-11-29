import os

os.system('cls')

numero_elementos = int(input('Quantos elementos na tupla: '))

elementos = []

for i in range (numero_elementos):
    while True:
        valor = input(f'Digite o valor {i + 1}: ')
        if valor.isdigit():
            elementos.append(int(valor))
            break
        else:
            print("Entrada inválida. Digite um número.")

tupla = tuple(elementos)

print('-'*70)

print(f'Tupla criada: {tupla}')
print('-'*70)

while True:

    valor = int(input('Verificar o número na Tupla: '))

    if valor in tupla:
        print(f"O número {valor} está na tupla")
        contagem = tupla.count(valor)
        print(f"O número {valor} aparece {contagem} vez(es)")

        indice = tupla.index(valor)
        print(f"A 1ª ocorrência de {valor} está no índice {indice}.")

    else:
        print(f"O numero {valor} não está na tupla.")

    continuar = input("Deseja continuar? (s/n): ").lower()
    if continuar != 's':
        print("Encerrando o programa. Até mais!")
        break
print('-'*70)
print('Fim do programa!')
print()