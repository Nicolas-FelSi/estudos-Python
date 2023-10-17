preco_produto = float(input('Qual é o preço do produto? R$'))
desconto = 5/100
produto_desconto = preco_produto - (preco_produto*desconto)

print(f'O produto que custava R${preco_produto}, na promoção com desconto de 5% vai custar R${produto_desconto:.2f}.')