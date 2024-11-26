# Faça um programa que preencha uma lista com as notas de 4 alunos, depois imprima a média.
import os
os.system('cls')

lista = []
soma = 0

for nota in range(1, 5):
    nota =  int(input('Digite a nota do aluno: '))
    lista.append(nota)
    soma += nota
print(f'{lista}')
print(soma)

media = soma / 4
print(media)