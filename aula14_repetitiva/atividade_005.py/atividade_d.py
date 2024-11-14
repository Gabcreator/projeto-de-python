#Faça um programa que imprima os números pares entre 0 e 100.
import os

os.system('cls')

for par in range (1, 101):
    
    if( par % 2 == 0):

        print(par,end= "|")