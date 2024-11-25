# Faça um programa que procure na lista numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15] e produza:
# • O intervalo de 1 até 9
# • O intervalo de 8 até 13
# • Os números pares
# • Os números ímpares
# • Os múltiplos de 2, 3 e 4
# • Lista reversa
# • O produto dos intervalos 5-6 por 11-12

import os

os.system('cls')

lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]


# intervalo (1 a 9)
for i in range (1, 10):
    print(f'seu intervalo de 1 a 9 foi {i}')

# intervalo (8 a 13)
for a in range (8, 14):
    print(f'seu intervalo de 8 a 13 foi {a}')

# intervalo (com números pares)
for f in range (1, 16):
    if f % 2 == 0:
        print(f'seus pares da lista são: {f}')
    else:
        print(f'seus ímpares da lista são: {f}')



# multiplos
for u in range(1, 16):
    if u % 2 == 0:

        print(f'os múltiplos de 2 nesta lista são: {u}')

for p in range(1, 16):
    if p % 3 == 0:

        print(f'os múltiplos de 3 nesta lista são: {p}')

for l in range(1, 16):
    if l % 4 == 0:


        print(f'os múltiplos de 4 nesta lista são: {l}')
# reversa
inverso = lista[::-1]
print(f'sua lista reversa ficou: {inverso}')


# intervalos
    
produto =  lista[5] * lista[11]

print(f'o seu produto foi: {produto}')

produto2 = lista[6] * lista[12]

print(f'o seu produto foi: {produto2}')