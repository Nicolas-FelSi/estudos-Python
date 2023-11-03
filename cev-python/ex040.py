primeira_nota = float(input('Primeira nota: '))
segunda_nota = float(input('Segunda nota: '))
media = (primeira_nota+segunda_nota)/2

print(f'Tirando {primeira_nota:.1f} e {segunda_nota:.1f}, a média do aluno é {media:.1f}')

if media >= 0 and media < 5:
    print('O aluno está REPROVADO.')
elif media >= 5 and media <= 6.9:
    print('O aluno está de RECUPERAÇÃO.')
elif media >= 7 and media <= 10:
    print('O aluno está APROVADO.')
else:
    print('Notas inválidas.')