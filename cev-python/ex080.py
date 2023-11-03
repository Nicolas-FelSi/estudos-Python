lista_numeros = []

for c in range(0, 5):
    valor = int(input('Digite um valor: '))
    if len(lista_numeros) == 0 or valor > lista_numeros[-1]:
        print('Adicionado ao final da lista...')
        lista_numeros.append(valor)
    else:
        pos = 0
        while pos < len(lista_numeros):
            if valor <= lista_numeros[pos]:
                lista_numeros.insert(pos, valor)
                print(f'Adicionado na posição {pos} da lista...')
                break
            pos += 1

print('-='*15)
print(f'Os valores digitados em ordem foram {lista_numeros}')