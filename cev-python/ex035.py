print('-='*20)
print('Analisador de Triângulos')
print('-='*20)

reta1 = float(input('Primeiro segmento: '))
reta2 = float(input('Segundo segmento: '))
reta3 = float(input('Terceiro segmento: '))

resultado1 = (reta1 + reta2) > reta3
resultado2 = (reta1 + reta3) > reta2
resultado3 = (reta3 + reta2) > reta1

if resultado1 and resultado2 and resultado3:
    print('Os segmentos acima PODEM FORMAR triângulo!')
else:
    print('Os segmentos acima NÃO PODEM FORMAR triângulo!')