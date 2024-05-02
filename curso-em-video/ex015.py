dias_alugados = int(input("Quantos dias alugados? "))
km_rodados = int(input("Quantos Km rodados? "))
valor = (60*dias_alugados) + (0.15*km_rodados)

print(f"O total a pagar é de R${valor:.2f}")