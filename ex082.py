lista_pares = []
lista_impares = []
lista_numeros = []

while True:
    lista_numeros.append(int(input('Digite um número: ')))
    continuar = ' '
    while continuar not in 'SN':
        continuar = input('Quer continuar? [S/N] ').strip().upper()
    if continuar == 'N':
        break
    
print('-='*15)
print(f'A lista completa é {lista_numeros}')

for num in lista_numeros:
    if num % 2 == 0:
        lista_pares.append(num)
    else:
        lista_impares.append(num)
        
print(f'A lista de pares é {lista_pares}')
print(f'A lista de ímpares é {lista_impares}')