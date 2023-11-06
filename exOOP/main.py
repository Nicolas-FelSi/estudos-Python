from cachorro import Cachorro
from gato import Gato
from dono import Dono


lista_cachorro = []
lista_gato = []
while True:
    print('-'*20)
    print('1. Cadastrar usuário')
    print('2. Cadastrar cachorro')
    print('3. Cadastrar gato')
    print('4. Listar cachorros')
    print('5. Listar gatos')
    print('6. Brincar com cachorros')
    print('7. Brincar com gatos')
    print('8. Sair')
    print('-'*20)

    opcao = int(input('Digite o número da opção: '))
    global dono
    if opcao == 1:
        nome_usuario = input('Digite seu nome: ').strip().title()
        dono = Dono(nome_usuario)
    elif opcao == 2:
        nome_cachorro = input('Nome do cachorro: ').strip().title()
        idade_cachorro = int(input('Idade do cachorro: '))
        cor_cachorro = input('Cor do cachorro: ').strip().title()
        qnt_brinq_cachorro = int(input('Quantidade de brinquedos do cachorro: '))
        cachorro = Cachorro(nome_cachorro, idade_cachorro,
                            cor_cachorro, qnt_brinq_cachorro, dono=dono)
        lista_cachorro.append(cachorro)
    elif opcao == 3:
        nome_gato = input('Nome do gato: ').strip().title()
        idade_gato = int(input('Idade do gato: '))
        cor_gato = input('Cor do gato: ').strip().title()
        qnt_bolin_gato = int(input('Quantidade de bolinhas do gato: '))
        gato = Gato(nome_gato, idade_gato, cor_gato, qnt_bolin_gato, dono=dono)
        lista_gato.append(gato)
    elif opcao == 4:
        for cachorro in lista_cachorro:
            print(cachorro)
    elif opcao == 5:
        for gato in lista_gato:
            print(gato)
    elif opcao == 6:
        for cachorro in lista_cachorro:
            print(cachorro.brincar())
            if cachorro.felicidade > 5:
                print(cachorro.fazer_barulho())
    elif opcao == 7:
        for gato in lista_gato:
            print(gato.brincar())
            if gato.felicidade > 5:
                print(gato.fazer_barulho())
    elif opcao == 8:
        break
    else:
        print('Opção inválida.')
