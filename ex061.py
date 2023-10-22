print('-'*20)
print('Sequência de Fibonacci')
print('-'*20)
termos = int(input('Quantos termos você quer mostrar? '))
count = 0
anterior1 = 1
anterior2 = 0

print(f'{anterior2} -> {anterior1} -> ', end='')
while count <= termos-3:
    atual = anterior2 + anterior1
    print(f'{atual} -> ', end='')
    anterior2 = anterior1
    anterior1 = atual
    count += 1

print('FIM')