import os
os.system('cls')

frase = str(input('coloque uma frase: '))
palavra = str(input('coloque uma palavra: '))

if(palavra in frase):
    print("tem")
else:
    print("nao tem")
    