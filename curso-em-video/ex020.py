from random import sample

aluno1 = str(input("Primeiro aluno: "))
aluno2 = str(input("Segunda aluno: "))
aluno3 = str(input("Terceiro aluno: "))
aluno4 = str(input("Quarto aluno: "))

lista_alunos = [aluno1, aluno2, aluno3, aluno4]
aluno_sorteado = sample(lista_alunos, k=4)

print(f"A ordem de apresentação será {aluno_sorteado}")