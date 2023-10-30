def maior(*valores):
    maior_valor = 0
    print('-='*30)
    print('Analisando os valores passados...')
    for i in valores:
        print(f'{i}', end=' ')
    print(f'Foram informados {len(valores)} valores ao todo.')
    for i in range(0, len(valores)):
        if i == 0:
            maior_valor = valores[i]
        elif valores[i] > maior_valor:
            maior_valor = valores[i]
    print(f'O maior valor informado foi {maior_valor}')


maior(4, 76, 1, 6, 3, 7, 2)
maior(3,6,1,8,4,7,3,9)
maior(23, 76, 23, 86, 32, 85)
maior(1,7,2)
maior()