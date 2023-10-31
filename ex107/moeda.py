def aumentar(preco, aumento):
    aumento_preco = preco + (preco * (aumento/100))
    return f'Aumentando {aumento}%, temos R${aumento_preco}'


def diminuir(preco, desconto):
    preco_desconto = preco - (preco * (desconto/100))
    return f'Reduzindo {desconto}%, temos R${preco_desconto}'


def dobro(preco):
    return f'O dobro de R${preco} é R${preco*2}'


def metade(preco):
    return f'A metade de R${preco} é R${preco/2}'



