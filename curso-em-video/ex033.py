valor1 = int(input("Primeiro valor: "))
valor2 = int(input("Segundo valor: "))
valor3 = int(input("Terceiro valor: "))

maior_valor = valor1
menor_valor = valor1

if valor2 > valor1 and valor2 > valor3:
    maior_valor = valor2
if valor3 > valor1 and valor3 > valor2:
    maior_valor = valor3

if valor2 < valor1 and valor2 < valor3:
    menor_valor = valor2
if valor3 < valor1 and valor3 < valor2:
    menor_valor = valor3
    
print(f"O menor valor digitado foi: {menor_valor}")
print(f"O maior valor digitado foi: {maior_valor}")