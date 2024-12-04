# iniciando
import os
os.system('cls')

# Montando e mostrando a lista
jogosJ = {'Sonic', 'Far Cry 4', 'Fortnite', 'Roblox', 'Minecraft', 'Blood Strike'}
jogosR = {'Far cry 4', 'Battlefield',  'Fortnite', 'Red Dead Island'}
jogosA = {'Roblox', 'lovers', 'plants vs zombies battle for neigboville', 'Minecraft'}

print(f'Os jogos favoritos de joão são: {jogosJ}')
print('-'*70)
print(f'Os jogos favoritos de Ronald são: {jogosR}')
print('-'*70)
print(f'Os jogos favoritos de Arthur primo de João são: {jogosA}')
print('-'*70)

# Unindos as listas
jogos_unidos = jogosJ.union(jogosR, jogosA)
print(f'Os jogos favoritos de cada um em uma só lista é: {jogos_unidos}')

# Adicionando e removendo das listas
jogosJ.add('Letal Company')
print(f'João ganhou um jogo de Ronald e agora a lista dele é: {jogosJ}')
print('-'*70)

jogosJ.remove('Sonic')
print(f'João tem muitos jogos de Sonic e então ele teve que os desinstalar e agora a lista ficou: {jogosJ}')


print('-'*70)
jogosR.add('Fallout')
print(f'Ronald baixou mais um de seus jogos de tiro antigos e agora sua lista é: {jogosR}')

print('-'*70)
jogosA.add('Escape the Gungeons')
print(f'Arthur descobriu um novo jogo de dungeons e agora sua lista ficou: {jogosA}')

print('-'*70)
jogosA.remove('lovers')
print(f'Arthur, para conseguir baixar este novo jogo teve que excluir um de seus jogos: lovers {jogosA}')

print('-'*70)
jogosR.remove('Red Dead Island')
print(f'Ronald estava com a memória do computador cheia e ele teve que excluir um de seus jogos: Red Dead Island {jogosR}')

print('-'*70)
jogosJ.remove('Fortnite')
print(f'João teve o mesmo problema que Ronald e então ele teve que excluir um de seus jogos: Fortnite {jogosJ}')

print('-'*70)
jogosJ.remove('Far Cry 4')
print(f'João teve que excluir Far Cry 4 para poder jogar Blood strike com os amigos: {jogosJ}')

# Terminando os códigos
print('-'*70)
print(F'A lista de João depois das mudanças ficou: {jogosJ}')
print('-'*70)
print(f'A lista de Ronald depois das mudanças ficou: {jogosR}')
print('-'*70)
print(f'A lista de Arthur depois das mudanças ficou: {jogosA}')
print('-'*70)