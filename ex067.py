while True:
    valor = int(input('Quer ver a tabuada de qual valor? '))
    print('-'*35)
    if valor < 0:
        break
    for num in range(1, 11):
        print(f'{valor} x {num} = {valor*num}')
    print('-'*35)

print('PROGRAMA TABUADA ENCERRADO. Volte sempre!')
    