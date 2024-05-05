# Exercício Python 044: Elabore um programa que calcule o valor a ser pago por um produto, 
# considerando o seu preço normal e condição de pagamento:
# - à vista dinheiro/cheque: 10% de desconto
# - à vista no cartão: 5% de desconto
# - em até 2x no cartão: preço formal
# - 3x ou mais no cartão: 20% de juros

print(f"{'='*10} LOJAS NICOLAS {'='*10}")

preco_compra = float(input("Preço das compras: R$"))

print("""
FORMAS DE PAGAMENTO
[ 1 ] à vista dinheiro/cheque
[ 2 ] à vista cartão
[ 3 ] 2x no cartão
[ 4 ] 3x ou mais no cartão
""")

opcao = int(input("Qual é a opção? "))

if opcao == 1:
    preco_final = preco_compra-(preco_compra*(10/100))
elif opcao == 2:
    preco_final = preco_compra-(preco_compra*(5/100))
elif opcao == 3:
    preco_final = preco_compra
    print(f"Sua compra será parcelada em 2x de R${(preco_final/2):.2f} SEM JUROS")
elif opcao == 4:
    preco_final = preco_compra+(preco_compra*(20/100))
    parcelas = int(input("Quantas parcelas? "))
    print(f"Sua compra será parcelada em {parcelas}x de R${(preco_final/parcelas):.2f} COM JUROS")
else:
    preco_final = preco_compra
    print("Opção inválida")

print(f"Sua compra de R${preco_compra} vai custar R${preco_final:.2f} no final")