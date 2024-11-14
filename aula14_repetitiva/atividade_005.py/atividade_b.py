#Evolua o programa anterior para um código que pergunte ao usuário qual o intervalo que ele deseja ver  impresso.
import os 


os.system('cls')

numero1 = int(input('coloque o primeiro número: '))
numero2 = int(input('coloque o segundo número: '))

for intervalo in range (numero1 , numero2):
    print(intervalo,end= "|")