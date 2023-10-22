numero = int(input('Digite um número para calcular seu Fatorial: '))
count = numero
fatorial = 1
print(f'Calculando {numero}! = ', end='')

while count > 0:
    if count == 1:
        print(f'{count}', end=' ')
    else:
        print(f'{count} x', end=' ')
    fatorial *= count
    count -= 1

print(f'= {fatorial}')