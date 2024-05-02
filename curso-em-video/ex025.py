nome_completo = str(input("Qual é o seu nome completo? ")).strip().lower()
nome_separado = nome_completo.split()

print(f"Seu nome tem Silva? {'silva' in nome_separado}")