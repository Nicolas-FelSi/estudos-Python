numero = int(input('Digite um número inteiro: '))

print('Escolha uma das bases para conversão: ')
print('[ 1 ] converter para BINÁRIO')
print('[ 2 ] converter para OCTAL')
print('[ 3 ] converter para HEXADECIMAL')

opcao = int(input('Sua opção: '))
 
if opcao == 1:
    numero_convertido = bin(numero)
    print(f'{numero} convertido para BINÁRIO é igual a {numero_convertido[2:]}')
elif opcao == 2:
    numero_convertido = oct(numero)
    print(f'{numero} convertido para OCTAL é igual a {numero_convertido[2:]}')
elif opcao == 3:
    numero_convertido = hex(numero)
    print(f'{numero} convertido para HEXADECIMAL é igual a {numero_convertido[2:]}')
else:
    print('Opção inválida.')
    