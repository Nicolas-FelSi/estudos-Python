# Exercício Python 070: Crie um programa que leia o nome e o preço de vários 
# produtos. O programa deverá perguntar se o usuário vai continuar ou não. 
# No final, mostre:
# A) qual é o total gasto na compra.
# B) quantos produtos custam mais de R$1000.
# C) qual é o nome do produto mais barato. 

print("-"*30)
print("      LOJA SUPER BARATÃO")
print("-"*30)

total_compra = produtos_mais_mil = produto_mais_barato_preco = contador = 0
produto_mais_barato_nome = " "

while True:
    nome_produto = str(input("Nome do produto: ")).strip()
    preco = float(input("Preço: R$"))
    
    total_compra += preco
    contador += 1
    
    if preco > 1000:
        produtos_mais_mil += 1
        
    if contador == 1 or preco < produto_mais_barato_preco:
        produto_mais_barato_preco = preco
        produto_mais_barato_nome = nome_produto
    
    continuar = " "
    while continuar not in "SN":
        continuar = str(input("Quer continuar? [S/N] ")).strip().upper()
        
    if continuar == "N":
        break


print(f"{'-'*10} FIM DO PROGRAMA {'-'*10}")

print(f"O total da compra foi R${total_compra:.2f}")
print(f"Temos {produtos_mais_mil} produtos custando mais de R$1000.00")
print(f"O produto mais barato foi {produto_mais_barato_nome} que custa R${produto_mais_barato_preco:.2f}")
