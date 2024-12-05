import os
os.system('cls')

cadastro = {
    'nome': 'Maria',
    'idade': 30,
    'profissão': 'engenharia'
}

print(cadastro['nome'])
cadastro['idade'] = 31
cadastro['cidade'] = 'São Paulo'
print(cadastro)