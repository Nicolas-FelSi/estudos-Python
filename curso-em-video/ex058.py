# Exercício Python 058: Melhore o jogo do DESAFIO 028 onde o 
# computador vai "pensar" em um número entre 0 e 10. 
# Só que agora o jogador vai tentar adivinhar até acertar, 
# mostrando no final quantos palpites foram necessários para vencer.

from random import randint
from time import sleep


print("Sou seu computador...")
sleep(0.5)
print("Acabei de pensar em um número entre 0 e 10.")
print("Será que você consegue adivinhar qual foi o número?")

computador = randint(0, 10)
jogador = int(input("Qual é o seu palpite? "))
tentativas = 1

while jogador != computador:
    tentativas += 1
    sleep(1)
    if computador > jogador:
        print("Mais... Tente mais uma vez.")
    else:
        print("Menos... Tente mais uma vez.")
        
    jogador = int(input("Qual é o seu palpite? "))

print(f"Acertou com {tentativas} tentativas. Parabéns!")

