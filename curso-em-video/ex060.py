# Exercício Python 060: Faça um programa que leia um número 
# qualquer e mostre o seu fatorial.
# Ex: 5! = 5 x 4 x 3 x 2 x 1 = 120

numero = int(input("Digite um número para calcular seu Fatorial: "))

print(f"Calculando {numero}! = ", end="")
total = 1

while numero > 0:
    if numero == 1:
        print(f"{numero} = ", end="")
    else:
        print(f"{numero} x ", end="")
    total *= numero
    numero -= 1

print(total)