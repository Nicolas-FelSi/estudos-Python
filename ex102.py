def fatorial(numero, show=False):
    '''
    -->Calcula o Fatorial de um número.
    :param n: O número a ser calculado.
    :param show: (opcional) Motrar ou não a conta.
    :return: O valor do Fatorial de um número n.
    '''
    print('-'*30)
    fatorial = 1
    for c in range(numero, 0, -1):
        if show:
            print(c, end=' ')
            if c > 1:
                print('x', end=' ')
            else:
                print('=', end=' ')
        fatorial *= c
    return fatorial
    
        

print(fatorial(5, False))
print(fatorial(8, False))
print(fatorial(7, True))
help(fatorial)