lista_pessoas = []
pessoa = []
maior_peso = menor_peso = 0

while True:
    pessoa.append(input('Nome: ').strip().title())
    pessoa.append(float(input('Peso: ')))
    
    continuar = ' '
    while continuar not in 'SN':
        continuar = input('Quer continuar? [S/N] ').strip().upper()
    
    if len(lista_pessoas) == 0:
        maior_peso = pessoa[1]
        menor_peso = pessoa[1]
    elif pessoa[1] > maior_peso:
        maior_peso = pessoa[1]
    elif pessoa[1] < menor_peso:
        menor_peso = pessoa[1]
        
    lista_pessoas.append(pessoa[:])
    pessoa.clear()
    
    if continuar == 'N':
        break

print('-='*15)
print(f'Ao todo, você cadastrou {len(lista_pessoas)} pessoas.')

print(f'O maior peso foi de {maior_peso}Kg. Peso de ', end='')
for pessoa in lista_pessoas:
    if pessoa[1] == maior_peso:
        print(f'{pessoa[0]}', end=' ')
        
print(f'\nO menor peso foi de {menor_peso}Kg. Peso de ', end='')
for pessoa in lista_pessoas:
    if pessoa[1] == menor_peso:
        print(f'{pessoa[0]}', end=' ')