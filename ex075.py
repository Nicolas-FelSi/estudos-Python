num1 = int(input('Digite um número: '))
num2 = int(input('Digite outro número: '))
num3 = int(input('Digite mais um número: '))
num4 = int(input('Digite o último número: '))
lista_numeros = (num1, num2, num3, num4)

print(f'Você digitou os valores {lista_numeros}')
print(f'O valor 9 apareceu {lista_numeros.count(9)} vezes')
print(f'O valor 3 apareceu na {lista_numeros.index(3)+1}ª posição')
print(f'Os valores pares digitados foram ', end='')

for c in lista_numeros:
    if c % 2 == 0:
        print(f'{c}', end=' ')
        

