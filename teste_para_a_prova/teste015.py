import os

os.system('cls')

print('1. soma = +1 ')
print('2. multiplicação = -1 ')
print('3. sair = 9999')

opcao = int(input('digite uma das opções: '))
valor = 0
valorm = 0

for a  in range (1, 10):
    if opcao == +1:
       if opcao == 9999:
           print('você saiu')
           break
       print('você selecionou soma (9999 para sair)')
       valor = opcao + 1
       valor1 = int(input('coloque o primeiro número: '))
       valor2 = int(input('coloque o segundo número: '))
       resultado = valor1 + valor2
       print(f'{resultado}')
    if opcao == -1:
        if opcao == 9999:
            print('você saiu')
            break
        print('você selecionou multiplicação (9999 para sair)')
        valor = opcao * 1
        valor3 = int(input('coloque um número para multiplicar: '))
        valor4 = int(input('coloque o segundo número para multiplicar: '))
        resultado_m = valor3 * valor4
        print(f'{resultado_m}')
    if opcao == 9999:
        print('você saiu')
        break