# Exercício Python 063: Escreva um programa que leia um número N inteiro
# qualquer e mostre na tela os N primeiros elementos de uma Sequência de Fibonacci. 
# Ex: 0 - 1 - 1 - 2 - 3 - 5 - 8

print("-"*30)
print("Sequência de Fibonacci")
print("-"*30)

termos = int(input("Quantos termos você quer mostrar? "))
contador = 0
primeiro = 0
segundo = 1

print("~"*30)
print(f"{primeiro} -> {segundo} -> ", end="")
while contador <= termos-3:
    terceiro = primeiro + segundo
    print(f"{terceiro} -> ", end="")
    
    primeiro = segundo
    segundo = terceiro
    contador += 1

print("FIM")

print("~"*30)