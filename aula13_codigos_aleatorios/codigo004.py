import os

os.system('cls')

nome = str(input('coloque o nome João Da Silva: '))

nome_alterado = nome.replace("Silva", "Oliveira")

print('-'*70)
print(f'o nome que era assim {nome} ficou assim {nome_alterado}')