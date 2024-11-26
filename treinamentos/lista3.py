import os 
os.system('cls')

animais = ['gato', 'cachorro', 'papagaio', 'jaguatirica', 'kaiky', 'guilherme']
nome = input('Digite um animal: ')
if nome in animais:
    print('este animal está na lista !!!')
else:
    print('infelismente agora você está devendo 1000$ ao governo !!!')