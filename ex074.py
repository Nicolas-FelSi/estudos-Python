from random import randint

lista_numeros = (randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10))
print('Os valores sorteados foram: ', end="")
for c in range(0, 5):
    if c != 4:
        print(lista_numeros[c], end=' ')
    else:
        print(lista_numeros[c])

print(f'O maior valor sorteado foi {max(lista_numeros)}')
print(f'O menor valor sorteado foi {min(lista_numeros)}')
