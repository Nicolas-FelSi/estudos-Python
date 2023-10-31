def ficha(nome, gols):
    return f'O jogador {nome} fez {gols} gol(s) no campeonato.'


nome = input('Nome do Jogador: ').strip().capitalize()
gols = input('Número de Gols: ').strip()
if gols.isnumeric():
    gols = int(gols)
elif gols == '' or not gols.isnumeric():
    gols = 0
else:
    print('Digite um valor válido.')

if nome == '':
    nome = '<desconhecido>'
print(ficha(nome, gols))
