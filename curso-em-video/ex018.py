import math

angulo = int(input("Digite um ângulo: "))
radiano = math.radians(angulo)

cosseno = math.cos(radiano)
seno = math.sin(radiano)
tangente = math.tan(radiano)

print(f"Angulo: {angulo}")
print(f"Cosseno: {cosseno:.2f}")
print(f"Seno: {seno:.2f}")
print(f"Tangente: {tangente:.2f}") 