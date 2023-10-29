from random import randint
from time import sleep

jogadas = {} 
ranking = {}

print('Valores sorteados: ')
for i in range(1, 5):
    jogadas[f'jogador{i}'] = randint(1, 6)

for k, v in jogadas.items():
    print(f'{k} tirou {v} no dado.')
    sleep(1)
    
print('-='*20)

ranking = sorted(jogadas.items(), key=lambda item:item[1], reverse=True)

print('== RANKING DOS JOGADORES  ==')
for pos, val in enumerate(ranking):
    print(f'{pos+1}º lugar: {val[0]} com {val[1]}.')

