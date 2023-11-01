def leia_dinheiro(preco):
    while True:
        if preco.isnumeric():
            preco = float(preco)
            return preco
        else:
            print(f'\033[1:31mERRO! {preco} é um preço inválido!\033[m')
            
            
