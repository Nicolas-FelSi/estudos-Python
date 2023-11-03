lista_numeros = []

for pos in range(0, 5):
    lista_numeros.append(int(input(f'Digite um valor para a Posição {pos}: ')))
    
maior_numero = max(lista_numeros)
menor_numero = min(lista_numeros)

print('=-'*15)
print(f'Você digitou os valores {lista_numeros}')
print(f'O maior valor digitado  foi {maior_numero} nas posições ', end='')
for pos, numero in enumerate(lista_numeros):
    if numero == maior_numero:
        print(f'{pos}...', end=' ')
        
print(f'\nO menor valor digitado  foi {menor_numero} nas posições ', end='')
for pos, numero in enumerate(lista_numeros):
    if numero == menor_numero:
        print(f'{pos}...', end=' ')