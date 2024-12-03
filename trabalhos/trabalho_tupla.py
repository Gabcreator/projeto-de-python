import os
os.system('cls')

numeros1 = {1, 2, 3, 4, 5}
numeros2 = {6, 7, 8, 9, 10}
numeros3 = {11, 12, 13, 14, 15}
numeros4 = {16, 17, 18, 19, 20}

juncao = numeros1.union(numeros2,numeros3)
print(juncao)

iguais = juncao.intersection(numeros2)
print(iguais)

diferente = numeros4.difference(numeros2)
print(diferente)

simetrica = numeros4.symmetric_difference(numeros3)
print(simetrica)

intercessao = numeros4.intersection(numeros2)
print(intercessao)

subconjunto = numeros3.issubset(numeros2)
print(subconjunto)

descartar = numeros1.discard(numeros2)
print(descartar)

