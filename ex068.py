from random import randint

print('=-'*15)
print('VAMOS JOGAR PAR OU ÍMPAR')
print('=-'*15)

cont = 0

while True:
    valor = int(input('Diga um valor: '))
    tipo = ' '
    while tipo not in 'PI':
        tipo = input('Par ou ímpar: [P\I] ').strip().upper()
    computador = randint(0, 10)
    soma = valor + computador
    par = soma % 2 == 0
    print('-'*30)
    print(f'Você jogou {valor} e o computador {computador}. Total de {soma}', end=' ')
    
    if par:
        print('DEU PAR')
        print('-'*30)
    else:
        print('DEU ÍMPAR')
        print('-'*30)
        
    if tipo == 'P' and par:
        print('Você VENCEU!')
        print('Vamos jogar novamente...')
        print('=-'*15)
        cont += 1
    elif tipo == 'I' and not par:
        print('Você VENCEU!')
        print('Vamos jogar novamente...')
        print('=-'*15)
        cont += 1
    else:
        print('Você PERDEU!')
        print('=-'*15)
        break
    
print(f'GAME OVER! Você venceu {cont} vezes.')