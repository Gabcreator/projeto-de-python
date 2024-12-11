# Faça um programa para criar um dicionário com pelo menos 4 elementos.
# O programa deve permitir que o usuário insira as chaves e os valores.
# As chaves devem ser únicas, e o programa deve garantir isso.
# Após inserir todos os elementos, o programa deve exibir o dicionário ordenado pelas chaves
import os
os.system('cls')

quantidade = int(input("Digite a quantidade desejada: "))
while True:
    print("1. Quantos elementos você quer colocar")
    print("2. Adicionar as chaves")
    print("3. Adicionar os valores")
    print("4. Mostrar o dicionário")
    print("5. Sair")
    
    opcao = input("Digite uma opção: ")

    if opcao == '1':
        quantidade = int(input("Digite a quantidade desejada: "))
        opcao = input("Digite uma opção (2, 5): ")

        for i in range (1, quantidade):
            if opcao == '2':
                chaves = input("Digite um a chave: ")
                print(f"As chaves {chaves} foram adicionadas no seu dicionário")
            elif opcao == '3':
                valor = input("Digite os valores: ")
                print(f"Os seus valores {valor} foram adicionadas no seu dicionário")
            elif opcao == '4':
                dicionario = len(opcao)
                print(f"seu dicionário final com as chaves e os valores foi {dicionario}.")

            elif opcao == '5':
                print("Saindo do programa")
                break

    else:
        print("Opção inválida. Tente novamente")