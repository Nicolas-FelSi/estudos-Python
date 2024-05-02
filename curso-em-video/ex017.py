# from math import pow, sqrt
from math import hypot

cateto_oposto = float(input("Comprimento do cateto oposto: "))
cateto_adjacente = float(input("Comprimento do cateto adjacente: "))
# hipotenusa = sqrt((pow(cateto_oposto,2) + pow(cateto_adjacente,2)))
hipotenusa = hypot(cateto_oposto, cateto_adjacente)

print(f"A hipotenusa vai medir {hipotenusa:.2f}")