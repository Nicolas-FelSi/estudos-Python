# Exercício Python 061: Refaça o DESAFIO 051, lendo o 
# primeiro termo e a razão de uma PA, mostrando os 10 primeiros 
# termos da progressão usando a estrutura while.

print("Gerador de PA")
print("-="*15)

primeiro = int(input("Primeiro termo: "))
razao = int(input("Razão da PA: "))
contador = 0

while contador < 10:
    print(f"{primeiro} ->", end=" ")
    primeiro += razao
    contador += 1
    
print("Fim")