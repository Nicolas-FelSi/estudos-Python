def leiaInt(numero):
    while True:
        numero_int = input(numero).strip()
        if numero_int.isnumeric():
            numero_int = int(numero_int)
            return numero_int
        else:
            print('\033[1;31mERRO! Digite um número inteiro válido.\033[m')


numero = leiaInt('Digite um número: ')
print(f'Você acabou de digitar o número {numero}.')
