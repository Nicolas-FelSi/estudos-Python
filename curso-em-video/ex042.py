# Exercício Python 042: Refaça o DESAFIO 035 dos triângulos, 
# acrescentando o recurso de mostrar que tipo de triângulo será formado:
# - EQUILÁTERO: todos os lados iguais
# - ISÓSCELES: dois lados iguais, um diferente
# - ESCALENO: todos os lados diferentes

print("-="*15)
print("Analisador de Triângulos")
print("-="*15)

seg1 = float(input("Primeiro segmento: "))
seg2 = float(input("Segundo segmento: "))
seg3 = float(input("Terceiro segmento: "))

if seg1 == seg2 == seg3: 
    print("Os segmentos acima PODEM FORMAR um triângulo EQUILÁTERO")
elif seg1 == seg2 != seg3 or seg1 == seg3 != seg2:
    print("Os segmentos acima PODEM FORMAR um triângulo ISÓSCELES")
elif seg1 != seg2 != seg3 != seg1:
    print("Os segmentos acima PODEM FORMAR um triângulo ESCALENO")   
else:
    print("Os segmentos acima NÃO PODEM FORMAR um triângulo")