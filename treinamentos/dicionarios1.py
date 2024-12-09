import os

os.system('cls')

while True:

    print('-'*70)
    print('\nLista para vender')
    print('1. Espada flamejante: 150 golds / dano: (60) / dano/p/s: (20) / defesa: (32)')
    print('2. Armadura de Reflexão: 120 golds / defesa: 50 / dano: (20% do dano recebido)')
    print('3. Poção da invisibilidade g: 100 golds / tempo de invisibilidade (60s)')
    print('4. Sair da Loja')

    opcao = input("O que você quer comprar?")

    if opcao == '1':
        print('Você comprou a Espada Flamejante por 150 golds')

    elif opcao == '2':
        print('Você comprou a Armadura de Reflexão por 120 golds')
    
    elif opcao == '3':
        print('Você comprou a Poção da Invisibilidade Grande por 100 golds')

    elif opcao == '4':
        print('Uma boa aventura para você meu velho aventureiro')
        break
    
    else:
        print('Me desculpe aventureiro mais não da para você comprar vento')