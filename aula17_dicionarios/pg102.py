import os
os.system('cls')

meu_dicionario = {}

while True:
    print('-'*70)
    print('\nMenu de Opções')
    print("1. Adicionar um par chave-valor")
    print("2. Remover um item usando pop()")
    print("3. Remover o ultimo item usando popitem()")
    print("4. Mostrar dicionário atual")
    print("5. Sair")
    print('-'*70)

    opcao = input("Escolha uma opção (1-5): ")

    if opcao == '1':
        chave = input("Digite a chave: ")
        valor = input("Digite o valor: ")
        meu_dicionario[chave] = valor
        print(f'Par {chave}: {valor} adicionado')

    elif opcao == '2':
        if meu_dicionario:
            chave = input("Digite a chave do item que deseja remover: ")
            valor_removido = meu_dicionario.pop(chave, "chave não encontrada")
            print(f"item removido: {chave}: {valor_removido}")
        else:
            print("O dicionário está vazio. adicione itens primeiro")

    elif opcao == '3':
        