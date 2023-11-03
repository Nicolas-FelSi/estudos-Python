from random import randint

print('Sou seu computador...')
tentativa = 0
computador = randint(0, 10)
print('Acabei de pensar em um número entre 0 e 10.')
print('Será que você consegue adivinhar qual foi?')
palpite = ''

while palpite != computador:
    palpite = int(input('Qual é o seu palpite? '))
    if palpite > computador:
        print('Menos... Tente mais uma vez.')
    elif palpite < computador:
        print('Mais... Tente mais uma vez.')
    tentativa += 1

print(f'Acertou com {tentativa} tentativas. Parabéns!')