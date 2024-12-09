import os

os.system('cls')

print('-'*70)
print('-------Tabela periódica-----------')
print('='*70)

elementos = {}
periodica = []

while True:
    
    print('-'*70)
    print('MENU DE OPÇÕES')
    print('='*70)
    print('1. Adicionar um elemento')
    print('2. Visualizar todos os elementos')
    print('3. Atualizar um elemento')
    print('4. Remover um elemento')
    print('5. Sair')

    opcao = input('Digite uma opção: ')

    if opcao == '1':
        simbolo = str(input('Simbolo do elemento: '))
        nome = str(input('Nome do elemento: '))
        elementos['simbolo'] = simbolo
        elementos['nome'] = nome
        periodica.append(elementos.copy())
        input("\nElemento adicionado. Pressione Enter para continuar...")

    elif opcao == '2':
        print('\nElementos na tabela periódica')
        print('-'*70)
        for elemento in periodica:
            for chave, valor in elemento.items():
                print(f'{chave.captalize()}: {valor}')
            print('-'*70)
        input("\nPressione Enter para continuar...")

    elif opcao == '3':
        simbolo = str(input('Digite o símbolo do elemento para atualizar: '))

        encontrado = False
        for elemento in periodica:
            if elemento['simbolo'] == simbolo:
                novo_simbolo = str(input('Digite o símbolo do elemento para '
                f'{simbolo} (ou deixe em branco manter atual)'))
                novo_nome = str(input('Digite o novo nome para: '
                f'{nome} (ou deixe em branco manter atual)'))
                
                if novo_simbolo:
                    elemento['simbolo'] = novo_simbolo
                if novo_nome:
                    elemento['nome'] = novo_nome

                encontrado = True
                break

        if encontrado:
            input('\nElemento atualizado. Enter para continuar...')
        else:
            input("\nElemento não atualizado. Enter para continuar...")