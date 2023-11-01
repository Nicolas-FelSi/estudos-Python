def aumentar(preco=0, aumento=0):
    aumento_preco = preco + (preco * (aumento/100))
    return moeda(aumento_preco)


def diminuir(preco=0, desconto=0):
    preco_desconto = preco - (preco * (desconto/100))
    return moeda(preco_desconto)


def dobro(preco=0):
    preco_dobro = preco*2
    return moeda(preco_dobro)


def metade(preco=0):
    preco_metade = preco/2
    return moeda(preco_metade)


def moeda(numero, moeda='R$'):
    return f'{moeda}{numero:.2f}'.replace('.', ',')


def resumo(preco=0, aumento=0, desconto=0):
    print('-'*30)
    print('{:>7}RESUMO DO VALOR'.format(''))
    print('-'*30)
    print(f'Preço analisado:{moeda(preco):>12}')
    print(f'Dobro do preço:{dobro(preco):>13}')
    print(f'Metade do preço{metade(preco):>13}')
    print(f'{aumento}% de aumento:{aumentar(preco, 20):>14}')
    print(f'{desconto}% de desconto:{diminuir(preco, 12):>13}')
    
