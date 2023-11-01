def leia_int(msg):
    while True:
        try:      
            numero = int(input(msg))
        except (ValueError, TypeError):
            print('\033[1;31mERRO! por favor, digite um número inteiro válido.\033[m')
            continue
        except (KeyboardInterrupt):
            print('\033[1;31mEntrada de dados interrompida pelo usuário.\033[m')
            return 0
        else:
            return numero


def leia_float(msg):
    while True:
        try:
            numero = float(input(msg))
        except (ValueError, TypeError):
            print('\033[1;31mERRO! por favor, digite um número real válido.\033[m')
            continue
        except (KeyboardInterrupt):
            print('\033[1;31mEntrada de dados interrompida pelo usuário.\033[m')
            return 0
        else:
            return numero


numero_int = leia_int('Digite um número inteiro: ')
numero_float = leia_float('Digite um número real: ')
print(f'O valor inteiro digitado foi {numero_int} e o real {numero_float}')
