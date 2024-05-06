# Exercício Python 052: Faça um programa que leia um número
# inteiro e diga se ele é ou não um número primo.

numero = int(input("Digite um número inteiro: "))
contador = 0

for i in range(1, numero+1):
    if numero % i == 0:
        print(f"\033[0;32m{i}\033[m", end=" ")
        contador += 1
    else:
        print(f"\033[1;31m{i}\033[m", end=" ")

print(f"\nO número {numero} foi divisível {contador} vezes")
    
if numero > 0 and contador > 2:
    print("E por isso ele NÃO É PRIMO!")
elif numero > 0 and contador <= 2:
    print("E por isso ele É PRIMO!")
else:
    print("Número inválido")
    