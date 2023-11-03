from time import sleep
from operator import neg


def contador(inicio, fim, passo):
    print('-='*30)
    if passo == 0:
        passo = 1
    elif passo < 0:
        passo = neg(passo)
    print(f'Contagem de {inicio} até {fim} de {passo} em {passo}')

    if inicio > fim:
        for i in range(inicio, fim-1, -passo):
            print(i, end=' ', flush=True)
            sleep(0.5)
    else:
        for i in range(inicio, fim+1, passo):
            print(i, end=' ', flush=True)
            sleep(0.5)
    print('FIM!', end='')
    print()


contador(1, 10, 1)
contador(10, 0, 2)
print('-='*30)
print('Agora é sua vez de personalizar a contagem!')
contador(
    int(input('Início: ')),
    int(input('Fim: ')),
    int(input('Passo: '))
)
