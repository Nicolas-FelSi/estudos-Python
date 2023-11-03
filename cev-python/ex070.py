print('-'*30)
print('{:^6}LOJA SUPER BARATÃO'.format(' '))
print('-'*30)

total = 0
produto_1000 = 0
cont = 0
produto_barato = 0

while True:
    produto = input('Nome do produto: ').strip().title()
    preco = float(input('Preço: R$'))
    continuar = ' '
    while continuar not in 'SN':
        continuar = input('Quer continuar? [S/N] ').strip().upper()
    
    total += preco
    cont += 1
    
    if preco > 1000:
        produto_1000 += 1
    if cont == 1 or preco < produto_barato:
        nome_produto_barato = produto
        produto_barato = preco
        
    if continuar == 'N':
        break

print('{:-^10}'.format('FIM DO PROGRAMA'))
print(f'O total da compra foi R${total:.2f}')
print(f'Temos {produto_1000} produtos custando mais de R$1000.00')
print(f'O produto mais barato foi {nome_produto_barato} que custa R${produto_barato:.2f}')