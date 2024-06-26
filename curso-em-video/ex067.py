# Exercício Python 067: Faça um programa que mostre a tabuada de vários 
# números, um de cada vez, para cada valor digitado pelo usuário. 
# O programa será interrompido quando o número solicitado for negativo.

while True:
    valor = int(input("Quer ver a tabuada de qual valor? "))

    print("-"*30)

    if valor < 0:
        break
    
    for i in range(1, 11):
        print(f"{valor} x {i} = {valor*i}")
    
    print("-"*30)
    

print("PROGRAMA TABUADA ENCERRADO. Volte sempre!")