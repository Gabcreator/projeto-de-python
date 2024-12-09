import os

os.system('cls')

meu_dicionario = {}

while True:
    print('-'*70)
    print("\nMenu de opções")
    print('1. Adicionar um par chave-valor')
    print('2. Definir valor padrão para uma chave usando setdeafult()')
    print('3. Atualizar o dicionário usando update()')
    print('4. Mostrar dicionário atual')
    print('5. Sair')
    print('-'*70)

    opcao = input('escolha uma opção: ')

    if opcao == '1':
        chave = input('Digite a chave: ')
        valor = input('Digite o valor: ')
        meu_dicionario = valor
        print(f'Par {chave}: {valor} adicionado')

    elif opcao == '2':
        chave = input("Digite a chave para definir um valor padrão: ")
        valor_padrao = input("Digite o valor padrão: ")
        valor_existente = meu_dicionario.setdefault(chave, valor_padrao)
        print(f"Valor para a chave '{chave}': {valor_existente}")

    elif opcao == 3:
        novos_pares = input("Digite os novos pares chave-valor"\
                            "No formato chave1:chave1,chave2:chave2: ")
        novos_pares_lista = novos_pares.split(',')
        novos_dados = {}
        for par in novos_pares_lista:
            chave, valor = par.split(',')
            novos_dados[chave] = valor
        meu_dicionario.update(novos_dados)
        print("Dicionário atualizado:", meu_dicionario)

    elif opcao == '4':
        
        if meu_dicionario:
            print("Dicionário atual", meu_dicionario)
        else:
            print("O dicionário está vazio")

    elif opcao == '5':

        print("Saindo do programa.")
        break

    else:
        print("Opção inválida. Tente novamente.")