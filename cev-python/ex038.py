primeiro_numero = int(input('Primeiro número: '))
segundo_numero = int(input('Segundo número: '))

if primeiro_numero > segundo_numero:
    print('O PRIMEIRO valor é maior')
elif segundo_numero > primeiro_numero:
    print('O SEGUNDO valor é maior')
elif segundo_numero == primeiro_numero:
    print('Os valores são iguais')
else:
    print('Valores inválidos. Tente novamente.')