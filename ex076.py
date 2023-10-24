print('-'*30)
print('{:^6}LISTAGEM DE PREÇOS'.format(' '))
print('-'*30)

lista_produtos = ('Lápis', 1.75, 'Borracha', 2.00,'Caderno', 15.90,'Estojo', 25.00,'Transferidor', 4.20,'Compasso', 9.99,'Mochila', 120.32,'Canetas', 22.30,'Livro', 34.90)

for i in range(0, len(lista_produtos), 2):
    print(f'{lista_produtos[i]:.<20}', end='')
    print(f'R$ {lista_produtos[i+1]:>6.2f}')

print('-'*30)
