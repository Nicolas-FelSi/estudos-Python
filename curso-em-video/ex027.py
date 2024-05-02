nome_completo = str(input("Digite seu nome completo: ")).strip().title()
nome_separado = nome_completo.split()

print(f"Seu primeiro nome é {nome_separado[0]}")
print(f"Seu último nome é {nome_separado[-1]}")