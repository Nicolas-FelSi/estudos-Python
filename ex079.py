lista_numeros = []

while True:
    numero = int(input('Digite um valor: '))
    if numero in lista_numeros:
        print('Valor duplicado! Não vou adicionar...')
    else:
        lista_numeros.append(numero)
        print('Valor adicionado com sucesso...')
    continuar = ' '
    while continuar not in 'SN':
        continuar = input('Quer continuar? [S/N] ').strip().upper()
    if continuar == 'N':
        break
    
print('-='*15)
print(f'Você digitou os valores {sorted(lista_numeros)}')