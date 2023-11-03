jogador = {}
gols = []

jogador['nome'] = input('Nome do jogador: ').strip().capitalize()
partidas = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))

for i in range(0, partidas):
    gols.append(int(input(f'Quantos gols na partida {i+1}? ')))
    # jogador['total'] += gols[i]            1º forma de somar os gols da lista e por dentro do dicionário
# jogador['total'] = sum(gols)               2º forma de somar os gols da lista e por dentro do dicionário
jogador['gols'] = gols.copy()    
jogador['total'] = sum(gols) 

print('-='*20)
print(jogador)
print('-='*20)

for k, v in jogador.items():
    print(f'O  campo {k} tem o valor {v}')
print('-='*20)

print(f'O jogador {jogador["nome"]} jogou {partidas} partidas.')
for pos, gols in enumerate(jogador['gols']):
    print(f'=> Na partida {pos+1}, fez {gols} gols.')
print(f'Foi um total de {jogador["total"]} gols.')
    