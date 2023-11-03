numeros_por_extenso = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze', 'quatorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')

numero = int(input('Digite um número entre 0 e 20: '))

while True:    
    if numero < 0 or numero > 20:
        while numero < 0 or numero > 20:
            numero = int(input('Tente novamente. Digite um número entre 0 e 20: '))
    else:
        break
    
print(f'Você digitou o número {numeros_por_extenso[numero]}')
    