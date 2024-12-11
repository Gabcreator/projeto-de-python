# faça um programa que permita o usuário criar um dicionário com cinco cores como chaves e seus respectivos valores, que podem ser descrições ou códigos de cor.
# O programa deve oferecer a possibilidade de adicionar novas cores ou modificar o valor de uma cor existente, caso o usuário deseje.
# Após a criação do dicionário, o programa deve exibir o dicionário de cores ordenado alfabeticamente pelas chaves (cores) e, em seguida, gerar um relatório que mostre a quantidade de cores que começam com cada letra do alfabeto
# O relatório deve ser apresentado de forma ordenada, exibindo quantas cores existem para cada inicial.
import os
os.system('cls')

base = ['vermelho', 'verde', 'amarelo']
cores = set(base)
print(cores)
while True:
    print('\nMenu de opções')
    print('1. criação das cores')
    print('2. Modificar')
    print('3. remover')
    print('4. Sair')

    opcao = int(input("Digite uma opção: "))

    if opcao == 1:
        input("Digite as cores: ")

    elif opcao == 2:
        modificação = ("Deseja modificar algum item? (s/n)")
        if modificação == 's':
            print("continuando...")
            continue
        else:
            print("Voltando para o programa!!!")
            break
    
    elif opcao == 3:
        remover = input("Digite o que você quer remover: ")
        removido = cores.pop(remover)
        print(f"Você removeu {removido} de seu dicionário")
        recolocar = input("Você deseja reposicionar este item no seu dicionário?(s/n)")
        if recolocar == 's':
            cores.add(removido)
            print("Você recolocou este item em seu dicionário!!!")
        else:
            print("Voltando para o menu.")

    elif opcao == 4:
        print("Saindo do programa!!!")
        break

    else:
        ("Opção inválida. Tente novamente")