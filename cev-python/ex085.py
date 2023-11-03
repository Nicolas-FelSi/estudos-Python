lista_numeros = []
pares = []
impares = []

for i in range(1, 8):
    lista_numeros.append(int(input(f'Digite o {i}º valor: ')))

for num in lista_numeros:
    if num % 2 == 0:
        pares.append(num)
    else:
        impares.append(num)

print('-='*15)        
pares.sort()
impares.sort()
print(f'Os valores pares digitados foram: {pares}')
print(f'Os valores ímpares digitados foram: {impares}')