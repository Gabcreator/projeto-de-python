import os
os.system("cls")
 
notas = []
quantidade = 0
inversa = []
soma = 0
media = 0
inserir = input("digite uma nota.: ")
while inserir != "0" and inserir != "s":
    notas.append(inserir)
    soma += int(inserir)
    inserir = input("digite uma nota.: ")
 
quantidade = len(notas)
inversa = notas[::-1]
media = (soma / quantidade)
print("=" * 50)
print("saidas")
print(f"A lista tem {quantidade} notas")
print(f" lista na ordem de insercao : {notas}")
print(f" lista na ordem inversa : ")
for principal in range(0, quantidade):
    print(inversa[principal])
print(f"a soma das notas foi..: {soma}")
print(f"a media geral foi.: {media}")
print("=" * 50)