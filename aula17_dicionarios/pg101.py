import os
os.system('cls')

meu_dicionario = {}

while True:
    print('-'*70)
    print("\nMenu de opções")
    print("1. Adicionar um par chave-valor")
    print("2. Mostrar chaves do dicionário")
    print("3. Mostrar valores do dicionário")
    print("4. Mostrar itens do dicionário")
    print("5. Sair")
    print('-'*70)

    opcao = input("Digite uma opção(1, 5): ")

    if opcao == '1':
        chave = input("Digite a chave: ")
        valor = input("Digite o valor: ")
        meu_dicionario[chave] = valor
        print(f"Par {chave}: {valor} adicionado")

    elif opcao == '2':
        if meu_dicionario:
            print("Chaves do dicionário:", meu_dicionario.keys())
        else:
            print("O dicionário está vazio. adicione itens primeiro.")

    elif opcao == '3':
        if meu_dicionario:
            print("Valores do dicionário", meu_dicionario.values())
        else:
            print("O dicionário está vazio. adicione itens primeiro")

    elif opcao == '4':
        if meu_dicionario:
            print("itens no dicionário: ", meu_dicionario.items())
        else:
            print("O dicionário está vazio. adicione itens primeiro")

    elif opcao == '5':
        print("Saindo do programa.")
        break

    else:
        print("Opção inválida. Tente novamente")