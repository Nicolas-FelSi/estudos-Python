from time import sleep

primeiro_valor = int(input('Primeiro valor: '))
segundo_valor = int(input('Segundo valor: '))
opcao = 0

while opcao != 5:
    print("""
    [ 1 ] somar
    [ 2 ] multiplicar
    [ 3 ] maior
    [ 4 ] novos números
    [ 5 ] sair do programa
    """)
    opcao = int(input('>>>>> Qual é a sua opção? '))
    if opcao == 1:
        soma = primeiro_valor + segundo_valor
        print(f'A soma entre {primeiro_valor} + {segundo_valor} é {soma}')
    elif opcao == 2:
        multiplicacao = primeiro_valor * segundo_valor
        print(f'O resultado de {primeiro_valor} x {segundo_valor} é {multiplicacao}')
    elif opcao == 3:
        if segundo_valor > primeiro_valor:
            print(f'Entre {primeiro_valor} e {segundo_valor} o maior valor é {segundo_valor}')
        elif primeiro_valor > segundo_valor:
            print(f'Entre {primeiro_valor} e {segundo_valor} o maior valor é {primeiro_valor}')
        else:
            print(f'Os valores são iguais')
    elif opcao == 4:
        print('Informe os números novamente:')
        primeiro_valor = int(input('Primeiro valor: '))
        segundo_valor = int(input('Segundo valor: '))
    elif opcao == 5:
        print('Finalizando...')
        sleep(0.5)
    else:
        print('Opção inválida. Tente novamente.')
    print('=-'*15)

print('Fim do programa! Volte sempre!')