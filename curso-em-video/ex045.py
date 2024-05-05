# Exercício Python 045: Crie um programa que faça o computador 
# jogar Jokenpô com você.

from random import randint
from time import sleep

print("""
Suas opções:
[ 0 ] PEDRA
[ 1 ] PAPEL
[ 2 ] TESOURA
""")

jogador = int(input("Qual é a sua jogada? "))

sleep(0.5)
print("JO")
sleep(0.5)
print("KEN")
sleep(0.5)
print("PO!!!")
sleep(0.5)

computador = randint(0, 2)
itens = ("PEDRA", "PAPEL", "TESOURA")

print("-="*15)
print(f"Computador jogou {itens[computador]}")
print(f"Jogador jogou {itens[jogador]}")
print("-="*15)

if computador == 0 and jogador == 1:
    print("JOGADOR VENCE")
elif computador == 1 and jogador == 2:
    print("JOGADOR VENCE") 
elif computador == 2 and jogador == 0:
    print("JOGADOR VENCE")  
elif computador == 0 and jogador == 2:
    print("COMPUTADOR VENCE")  
elif computador == 1 and jogador == 0:
    print("COMPUTADOR VENCE")  
elif computador == 2 and jogador == 1:
    print("COMPUTADOR VENCE")    
elif computador == 0 and jogador == 0:
    print("EMPATE")    
elif computador == 1 and jogador == 1:
    print("EMPATE")  
elif computador == 2 and jogador == 2:
    print("EMPATE")   
else:
    print("Opção inválida")
