import os

os.system('cls')

print('-'*70)
print('SAÍDA COM FOR')
print('='*70)

lista_alunos = []

for c in range (0, 5):
    nome = str(input("Entre com o nome do aluno: "))

lista_alunos.append(nome)

print()
print('Impresão dos nomes de alunos:')

for aluno in range(len(lista_alunos)):
    print(lista_alunos[aluno], end=' ')
    if c == aluno:
        print()

print()
print('-'*70)
print("Fim do progrma!")
print('-'*70)
