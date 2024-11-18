import os

os.system('cls')

quantidade = 0
soma = 0

for variavel_impar in range (1, 101, 2):
    
    quantidade += 1
    soma += variavel_impar
    
print(f'são {quantidade} números ímpares e soma é {soma}')