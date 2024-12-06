import os

os.system('cls')

meu_dicionario = {}

while True:

    print('-'*70)
    print("\nMenu de opções")
    print("1. Criar um dicionário usando fromkeys()")
    print("2. Buscar valor de uma chave com get()")
    print("3. Sair")
    print('-'*70)

    opcoes = input("escolha uma opção: ")

    if opcoes == '1':

        chaves = input("Digite as chaves separadas por vírgula: ").split(',')
        valor_padrao = input("Digite o valor padrão para as chaves: ")

        if not chaves or not valor_padrao:
            print("Erro: Chaves ou valor padrão não podem ser vazios")
        else:
            meu_dicionario = dict.fromkeys(chaves, valor_padrao)
            print("Dicionário criado", meu_dicionario)
    elif opcoes == '2':

        if meu_dicionario:
            print("Chaves disponíveis: ", ", ".join(meu_dicionario.keys()))
            chave = input("Digite a chave que deseja buscar: ")
            valor = meu_dicionario.get(chave, "Chave não encontrada")
            print('-'*80)
            print(f"Valor para a chave '{chave}', {valor}")
        else:
            print('-'*70)
            print("Erro! Crie um dicionário primeiro.")

    elif opcoes == '3':
        print('Saindo do programa.')
        break
    
    else:
        print("Opção inválida. Tente novamente")