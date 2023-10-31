def aumentar(preco=0, aumento=0):
    aumento_preco = preco + (preco * (aumento/100))
    return f'Aumentando {aumento}%, temos {moeda(aumento_preco)}'


def diminuir(preco=0, desconto=0):
    preco_desconto = preco - (preco * (desconto/100))
    return f'Reduzindo {desconto}%, temos {moeda(preco_desconto)}'


def dobro(preco=0):
    return f'O dobro de {moeda(preco)} é {moeda(preco*2)}'


def metade(preco=0):
    return f'A metade de {moeda(preco)} é {moeda(preco/2)}'


def moeda(numero, moeda='R$'):
    return f'{moeda}{numero:.2f}'.replace('.', ',')
