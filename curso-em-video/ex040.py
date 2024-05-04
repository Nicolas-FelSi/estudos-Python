# Exercício Python 040: Crie um programa que leia duas notas de um aluno 
# e calcule sua média, mostrando uma mensagem no final, de acordo com a média atingida:
# - Média abaixo de 5.0: REPROVADO
# - Média entre 5.0 e 6.9: RECUPERAÇÃO
# - Média 7.0 ou superior: APROVADO

nota1 = float(input("Primeira nota: "))
nota2 = float(input("Segunda nota: "))
media = (nota1 + nota2)/2

print(f"Tirando {nota1} e {nota2}, a média do aluno é {media:.1f}")

if media >= 7 and media <= 10:
    print("O aluno está APROVADO")
elif media >= 5 and media < 7:
    print("O aluno está em RECUPERAÇÃO")
elif media >= 0 and media < 5:
    print("O aluno está REPROVADO")
else: 
    print("Nota inválida")