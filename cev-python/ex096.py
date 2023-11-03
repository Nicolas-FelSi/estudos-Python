# 1º FORMA
'''
def calcular_area():
    print('Controle de Terrenos')
    print('-'*20)
    largura = float(input('LARGURA (m): '))
    comprimento = float(input('COMPRIMENTO (m): '))
    area = largura*comprimento
    print(f'A área de um terreno {largura}x{comprimento} é de {area}m².')

calcular_area()
'''

# 2º FORMA
def calcular_area(largura, comprimento):
    area = largura*comprimento
    print(f'A área de um terreno {largura}x{comprimento} é de {area}m².')


print('Controle de Terrenos')
print('-'*20)
calcular_area(
    float(input('LARGURA (m): ')),
    float(input('COMPRIMENTO (m): '))
)
