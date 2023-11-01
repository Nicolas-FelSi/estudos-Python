from ex115.prints import linhas
from ex115.prints import menu

def leia_int(msg):
    while True:
        menu()
        opcao = 0
        if opcao == 3:
            break
        while True:
            try:
                opcao = int(input(msg))
            except (ValueError, TypeError):
                print('\033[1;31mERRO: por favor, digite um número inteiro válido.\033[m')
            except (KeyboardInterrupt):
                print('\033[1;31mEntrada de dados interrompida pelo usuário.\033[m')
            else:
                if opcao < 1 or opcao > 3:
                    print('\033[1;31mERRO! Digite uma opção válida.\033[m')   
                    continue
                else:  
                    if opcao == 3:
                        break
                    else:
                        linhas()
                        print('{:>11}Opção {}'.format('', opcao))
                        linhas()
                        break
        if opcao == 3:
            linhas()
            print('{:>}Saindo do sistema... Até logo!'.format(''))
            linhas()
            break