soma = 0
contador = 0

for count in range(1, 7):
    numero = int(input(f'Digite o {count} valor: '))
    if numero % 2 == 0:
        contador += 1
        soma += numero

print(f'Você informou {contador} números PARES e a soma foi {soma}')
    