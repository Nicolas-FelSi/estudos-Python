frase = input('Digite uma frase: ').strip().lower()
letra_a = frase.count('a')
primeira_letra_a = frase.index('a')
ultima_letra_a = frase.rfind('a')
print(f"""
A letra A aparece {letra_a} vezes na frase.
A primeira letra A apareceu na posição {primeira_letra_a + 1}
A última letra A apareceu na posição {ultima_letra_a + 1}
""")