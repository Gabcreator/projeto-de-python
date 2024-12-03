import os 
os.system

lista1 = {1, 2, 3}
lista2 = {4, 5, 6}

uniao = lista1.union(lista2)
print(uniao)

intersecao = lista1.intersection(lista2)
print(intersecao)

diferenca = lista1.difference(lista2)
print(diferenca)

diferenca_simetrica = lista1.symmetric_difference(lista2)
print(diferenca_simetrica)

subconjunto = lista1.issubset(lista2)
print(subconjunto)