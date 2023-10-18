from math import radians, sin, cos, tan
angulo = float(input('Digite o ângulo que você deseja: '))
radianos = radians(angulo)
print(f'O ângulo de {angulo} tem o SENO de {sin(radianos):.2f}')
print(f'O ângulo de {angulo} tem o COSSENO de {cos(radianos):.2f}')
print(f'O ângulo de {angulo} tem o TANGENTE de {tan(radianos):.2f}')