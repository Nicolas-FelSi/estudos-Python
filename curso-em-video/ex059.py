# Exercício Python 059: Crie um programa que leia dois valores
# e mostre um menu na tela:
# [ 1 ] somar
# [ 2 ] multiplicar
# [ 3 ] maior
# [ 4 ] novos números
# [ 5 ] sair do programa
# Seu programa deverá realizar a operação solicitada em cada caso.

from time import sleep

primeiro_valor = int(input("Primeiro valor: "))
segundo_valor = int(input("Segundo valor: "))

sair_programa = False
while not sair_programa:
    print(
    """    [ 1 ] somar
    [ 2 ] multiplicar
    [ 3 ] maior
    [ 4 ] novos números
    [ 5 ] sair do programa""")
    opcao = int(input(f">>>>> Qual é a sua opção? "))
    
    if opcao == 1:
        soma = primeiro_valor+segundo_valor
        print(f"A soma entre {primeiro_valor} + {segundo_valor} é {soma}")
    elif opcao == 2:
        multiplicacao = primeiro_valor * segundo_valor
        print(f"A multiplicação entre {primeiro_valor} x {segundo_valor} é {multiplicacao}")
    elif opcao == 3:
        if primeiro_valor > segundo_valor:
            print(f"Entre {primeiro_valor} e {segundo_valor} o maior valor é {primeiro_valor}")
        elif segundo_valor > primeiro_valor:
            print(f"Entre {primeiro_valor} e {segundo_valor} o maior valor é {segundo_valor}")
        else:
            print("Os números são iguais")
    elif opcao == 4:
        print("Informe os números novamente:")
        primeiro_valor = int(input("Primeiro valor: "))
        segundo_valor = int(input("Segundo valor: "))
    elif opcao == 5:
        print("Finalizando...")
        sleep(1)
        sair_programa = True
    else:
        print("Opção inválida")
    
    print("=-="*10)
    
print("Fim do programa! Volte sempre!")

    