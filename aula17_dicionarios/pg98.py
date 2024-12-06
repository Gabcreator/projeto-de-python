import os

os.system('cls')

meu_dicionario = {}

while True:
    print('-'*70)
    print("\nMenu de opções:")
    print("1. Adicionar chave-valor: ")
    print("2. Mostrar o Dicionário: ")
    print("3. Mostrar o tamanho do dicionário: ")
    print("4. Fazer uma cópia do dicionário: ")
    print("5. Limpar o dicionário: ")
    print("6. Sair")
    print('-'*70)
    
    opcao = input('Digite uma opção: ')

    if opcao == '1':

        chave = input("Digite a chave: ")

        while not chave:
            print("A chave não pode ser vazia: tente novamente")
            chave = input('Digite uma chave: ')

        valor = input("Digite um valor: ")
        while not valor:
            print("O valor não pode ser vazio. Tente novamente")
            valor = input("Digite um valor: ")

        meu_dicionario[chave] = valor
        print(f'Par {chave}: {valor} adicionario')

    elif opcao == '2':
        print("Dicionário atual: ", meu_dicionario)

    elif opcao == '3':
        tamanho = len(meu_dicionario)
        print(f"O dicionário tem {tamanho} valores")

    elif opcao == '4':
        copia_dicionario = meu_dicionario.copy()
        print(f"copia dicionário: ", meu_dicionario)

    elif opcao == '5':
        meu_dicionario.clear()
        print("Dicionário  limpo")

    elif opcao == '6':
        print("Saindo do programa")
        break

    else:
        print("Opção inválida. tente novamente")