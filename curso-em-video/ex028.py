from random import randint
from time import sleep

print("-="*30)
print("Vou pensar em um número entre 0 e 5. Tente adivinhar...")
print("-="*30)

numero_computador = randint(0, 5)

numero_jogador = int(input("Em que número eu pensei? "))
print("PROCESSANDO...")
sleep(3)

if numero_computador == numero_jogador:
    print("PARABÉNS! Você conseguiu me vencer!")
else:
    print(f"GANHEI! Eu pensei no número {numero_computador} e não no {numero_jogador}")

