import os 

os.system('cls')

Nome = str(input('coloque seu primeiro nome: '))
nome_do_meio = str(input('coloque seu nome do meio: '))
sobrenome = str(input('coloque seu sobrenome: '))

nome_completo = Nome + nome_do_meio + sobrenome.strip()

print(f'o seu nome completo ira ficar {nome_completo}')