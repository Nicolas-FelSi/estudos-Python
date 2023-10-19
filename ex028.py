from random import randint
from time import sleep

print('-='*30)
print('Vou pensar em um número entre 0 e 5. Tente advinhar...')
print('-='*30)

numero_random = randint(0, 5)
numero_digitado = int(input('Em que número estou pensando? '))

print('PROCESSANDO...')
sleep(1)

if numero_digitado == numero_random:
    print('PARABÉNS! Você conseguiu me vencer.')
else:
    print(f'GANHEI! Eu pensei no número {numero_random} e não no {numero_digitado}')


