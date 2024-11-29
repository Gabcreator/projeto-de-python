# aceite números até o usuário apertar 's' mostre a lista inversa quantos números tem na lista o número maior e o número menor
import os

os.system('cls')

lista = []

numero = input('Digite um número: ')
while (numero != 's'):
    lista.append(int(numero))
    numero = input('Digite um número: ')

lista_co = lista.copy()
# reverso
numero_r = lista.sort(reverse=True)
print(f'A sua lista invertida vai ser: {lista}')

# maior
print(f'O número maior de sua lista é: {lista[0]}')
# menor
print(f'O número menor de sua lista é: {lista[9]}')


print(f'A sua lista inteira é: {lista_co}')