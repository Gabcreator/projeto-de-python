#faça um sistema que faça o cliente colocar uma frase toda em maiusculo e depois converter todas menos a primeira letra em minusculo
import os
os.system('cls')

maiusculo = str(input('coloque uma frase toda em maiusculo: '))

convertida = maiusculo.capitalize()

print(f'a frase sem ser convertida ficou: {maiusculo}')
print(f'e a frase convertida ficou: {convertida}')