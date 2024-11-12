import os

os.system('cls')

print('-'*70)
print('ESTRUTURA DE CONTROLE WHILE ELSE BREAK')
print('-'*70)
print()

print()

while (True):

    nome = str(input('digite um nome [s para sair]: ')).lower()

    if(nome != 's'):
        print('continue digitando...')
    else:
        print('-'*70)
        print('Você digitou "s" para sair')

        break

print('-'*70)
print()