import os 

os.system('cls')

print('-'*70)
print('ESTRUTURA DE CONTROLE VALIDAÇÃO E CASTING')
print('-'*70)

soma = 0

for c in range(0, 5):
    numero = input('coloque um número [0-5]: ')

    if(not (numero.isnumeric())):
        print(f'"{numero}" Entrada inválida ')
        print()
    else:
        numero = int(numero)

        if (numero >= 0 and numero <= 5 ):
            print(f'o número {numero} está dentro do intervalo  [0, 5]')
            print()
        else:
            print(f'"{numero}" Entrada inválida!')
            print()

    print('-'*70)
print()