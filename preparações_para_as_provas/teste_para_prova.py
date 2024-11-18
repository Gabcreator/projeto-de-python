# seu cliente quer que você crie um programa que conte apenas ímpare
import os

os.system('cls')

inicio = int(input("diggitew inicio"))
fim = int(input("diggitew fim"))
passo = int(input("diggite escala"))


for var_impar in range(inicio, fim, passo):
    print(f'a sua conta de 1 a 100 {var_impar}', end= "|")

inicio = 1
fim = 101
passo = 2