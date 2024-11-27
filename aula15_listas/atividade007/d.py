# Crie uma lista com 6 nomes, depois verifique se o nome ‘Pedro’ está nessa lista.
import os
os.system('cls')

lista = []
nome_p = ('pedro')

for i in range (1, 7):
    nomes = input('Digite o nome de um amigo: ')
    lista.append(nomes)

if nome_p in lista:
    print('O nome pedro está na sua lista')
else:
    print('O nome Pedro não está na lista')