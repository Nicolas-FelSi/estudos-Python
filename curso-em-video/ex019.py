from random import choice

aluno1 = str(input("Primeiro aluno: "))
aluno2 = str(input("Segunda aluno: "))
aluno3 = str(input("Terceiro aluno: "))
aluno4 = str(input("Quarto aluno: "))

lista_alunos = [aluno1, aluno2, aluno3, aluno4]
aluno_sorteado = choice(lista_alunos)

print(f"O aluno sorteado foi {aluno_sorteado}")
