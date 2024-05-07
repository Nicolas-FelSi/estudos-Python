# Exercício Python 071: Crie um programa que simule o funcionamento de um 
# caixa eletrônico. No início, pergunte ao usuário qual será o valor a ser 
# sacado (número inteiro) e o programa vai informar quantas cédulas de cada 
# valor serão entregues.
# OBS: considere que o caixa possui cédulas de R$50, R$20, R$10 e R$1.

print("="*30)
print("        BANCO CEV")
print("="*30)

sacar = int(input("Que valor você quer sacar? R$"))
nota_50 = nota_20 = nota_10 = nota_1 = 0

while True:
    if sacar >= 50:
        sacar -= 50
        nota_50 += 1
    elif sacar >= 20:
        sacar -= 20
        nota_20 += 1
    elif sacar >= 10:
        sacar -= 10
        nota_10 += 1
    elif sacar >= 1:
        sacar -= 1
        nota_1 += 1
    else:
        break
    

print(f"Total de {nota_50} cédulas de R$50")    
print(f"Total de {nota_20} cédulas de R$20")   
print(f"Total de {nota_10} cédulas de R$10")   
print(f"Total de {nota_1} cédulas de R$1")   
print("="*30)
print("Volte sempe ao BANCO CEV! Tenha um bom dia!")