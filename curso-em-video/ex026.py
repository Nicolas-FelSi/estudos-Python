frase = str(input("Digite uma frase: ")).strip().lower()
letra_a = frase.count("a")
primeira_letra_a = frase.find("a")
ultima_letra_a = frase.rfind("a")

print(f"A letra A aparece {letra_a} vezes na frase.")
print(f"A primeira letra A apareceu na posição {primeira_letra_a}")
print(f"A última letra A apareceu na posição {ultima_letra_a}")