from random import randint
from time import sleep

numeros = []

def sorteia():
    print('Sorteando 5 valores da lista: ', end='')
    for i in range(0, 5):
        numeros.append(randint(1, 10))
        print(f'{numeros[i]}', end=' ', flush=True)
        sleep(0.5)
    print('PRONTO!')


sorteia()

def somaPar(lista):
    soma = 0
    for num in lista:
        if num % 2 == 0:
            soma += num
    print(f'Somando os valores pares de {lista}, temos {soma}')

somaPar(numeros)
        
          

    