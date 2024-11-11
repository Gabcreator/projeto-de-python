#seu cliente quer que você crie um sistema que coloque uma frase que coloque a frase que ele colocou em maiusculo e em minusculo
import os
os.system('cls')

frase = str(input('coloque uma frase: '))

frase_maiusculo = frase.upper()
frase_minusculo = frase.lower()

print(f'a frase em maiusculo ficou: {frase_maiusculo}')
print(f'e em minusculo ficou: {frase_minusculo}')