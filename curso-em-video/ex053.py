# Exercício Python 053: Crie um programa que leia uma frase 
# qualquer e diga se ela é um palíndromo, desconsiderando os espaços.

frase = str(input("Digite uma frase: ")).strip().upper()
frase_separada = frase.split()
frase_junta = "".join(frase_separada)
frase_invertida = frase_junta[::-1]

print(f"O inverso de {frase_junta} é {frase_invertida}")

if frase_junta == frase_invertida:
    print("A frase digitada é um palíndromo!")
else:
    print("A frase digitada não é um palíndromo!")