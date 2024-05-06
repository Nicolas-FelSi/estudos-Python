# Exercício Python 065: Crie um programa que leia vários números inteiros pelo teclado. 
# No final da execução, mostre a média entre todos os valores e qual foi o maior e o
# menor valores lidos. O programa deve perguntar ao usuário se ele quer ou não continuar 
# a digitar valores.

contador = media = soma = menor_valor = maior_valor = 0
continuar = ""

while continuar != "N":
    numero = int(input("Digite um número: "))
    continuar = str(input("Quer continuar? [S/N] ")).strip().upper()
    contador += 1
    soma += numero
    if contador == 1:
        maior_valor = numero
        menor_valor = numero
    elif numero > maior_valor:
        maior_valor = numero
    elif numero < menor_valor:
        menor_valor = numero
        

media = soma/contador

print(f"Você digitou {contador} números e a média foi {media:.2f}")
print(f"O maior valor foi {maior_valor} e o menor foi {menor_valor}")
    