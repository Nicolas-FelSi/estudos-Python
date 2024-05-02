preco = float(input("Digite o preço do produto: R$"))
preco_com_desconto = preco-(preco*(5/100))

print(f"De R${preco} vai para R${preco_com_desconto:.2f} com 5% de desconto.")