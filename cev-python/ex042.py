reta1 = float(input('Primeiro segmento: '))
reta2 = float(input('Segundo segmento: '))
reta3 = float(input('Terceiro segmento: '))

resultado1 = (reta1 + reta2) > reta3
resultado2 = (reta1 + reta3) > reta2
resultado3 = (reta3 + reta2) > reta1

equilatero = resultado1 == resultado2 == resultado3
escaleno = resultado1 != resultado2 != resultado3

if resultado1 and resultado2 and resultado3:
    if equilatero:
        print('Os segmentos acima PODEM FORMAR triângulo EQUILÁTERO!')
    elif escaleno:
        print('Os segmentos acima PODEM FORMAR triângulo ESCALENO!')
    else:
        print('Os segmentos acima PODEM FORMAR triângulo ISÓSCELES!')
else:
    print('Os segmentos acima NÃO PODEM FORMAR triângulo!')