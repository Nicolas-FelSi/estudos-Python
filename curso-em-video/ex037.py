numero = int(input("Digite um número inteiro: "))
print("""Escolha uma das bases para conversão:
[ 1 ] converter para BINÁRIO 
[ 2 ] converter para OCTAL
[ 3 ] converter para HEXADECIMAL""")

escolha = int(input("Sua opção: "))

if escolha == 1:
    # binario = bin(numero)
    # :b converte o valor em binário e retira os 2 valores da frente Ex:0b11101010 -> 11101010
    print(f"{numero} convertido para BINÁRIO é igual a {numero:b}")
elif escolha == 2:
    # octal = oct(numero)
    # :o converte o valor em octal e retira os 2 valores da frente Ex:0o352 -> 352
    print(f"{numero} convertido para OCTAL é igual a {numero:o}")
elif escolha == 3:
    # hexadecimal = hex(numero)
    # :x converte o valor em hexadecimal e retira os 2 valores da frente Ex:0xea -> ea
    print(f"{numero} convertido para HEXADECIMAL é igual a {numero:x}")
else:
    print("Opção inválida:")