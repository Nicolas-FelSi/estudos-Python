nome = str(input("Digite seu nome completo: ")).strip()
nome_separado = nome.split()
nome_sem_espaco = "".join(nome_separado)

print("Analisando seu nome...")
print(f"Seu nome em maiúsculas é {nome.upper()}")
print(f"Seu nome em minúsculas é {nome.lower()}")
print(f"Seu nome tem ao todo {len(nome_sem_espaco)} letras")
print(f"Seu primeiro nome é {nome_separado[0]} e ele tem {len(nome_separado[0])} letras")