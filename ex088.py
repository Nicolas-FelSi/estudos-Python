from random import randint
from time import sleep

lista_numeros = []

print('-'*30)
print('{:>6}JOGA NA MEGA SENA'.format(' '))
print('-'*30)

jogos = int(input('Quantos jogos você quer que eu sorteie? '))
sleep(0.5)

print('-='*3, end=' ')
print(f'SORTEANDO {jogos} JOGOS', end=' ')
print('-='*3)

for i in range(0, jogos):
    for j in range(0, 6):
        num = randint(1, 60)
        if num not in lista_numeros:
            lista_numeros.append(num)
    lista_numeros.sort()
    print(f'Jogo {i+1}: {lista_numeros}')
    lista_numeros.clear()
    sleep(0.5)

print('-='*5, end=' ')
print('< BOA SORTE! >', end=' ')
print('-='*5)