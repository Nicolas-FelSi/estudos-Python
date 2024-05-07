# Exercício Python 068: Faça um programa que jogue par ou ímpar 
# com o computador. O jogo só será interrompido quando o jogador perder, 
# mostrando o total de vitórias consecutivas que ele conquistou no final 
# do jogo. 

from random import randint

print("=-"*15)
print("VAMOS JOGAR PAR OU ÍMPAR")
print("=-"*15)

contador = 0

while True:   
    jogador = int(input("Diga um valor: "))
    
    par_ou_impar = " "
    while par_ou_impar not in "PI":
        par_ou_impar = str(input("Par ou Ímpar? [P/I] ")).strip().upper()
    
    computador = randint(0, 10)
    total = jogador + computador
    
    print("-"*30)
    print(f"Você jogou {jogador} e o computador {computador}. Total de {total}", end=" ")
    if total % 2 == 0:
        print("DEU PAR")
    else:
        print("DEU ÍMPAR")
    print("-"*30)
    
    if (par_ou_impar == "P" and total % 2 == 0) or (par_ou_impar == "I" and total % 2 != 0):
        print("Você VENCEU!")
        print("Vamos jogar novamente...")
        contador += 1
    else:
        print("Você PERDEU!")
        break
        
    print("=-"*15)
    
print(f"GAME OVER! Você venceu {contador} vezes.")