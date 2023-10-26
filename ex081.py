
lista_numeros = []

while True:
    lista_numeros.append(int(input('Digite um valor: ')))
    continuar = ' '
    while continuar not in 'SN':
        continuar = input('Quer continuar? [S/N] ').strip().upper()
    if continuar == 'N':
        break
    
print('-='*15)
print(f'Você digitou {len(lista_numeros)} elementos.')
lista_numeros.sort(reverse=True)
print(f'Os valores em ordem decrescente são {lista_numeros}')

if 5 in lista_numeros:
    print(f'O valor 5 faz parte da lista!')
else:
    print(f'O valor 5 não foi encontrado na lista!')