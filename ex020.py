from random import sample
primeiro_aluno =  input('Primeiro aluno: ') 
segundo_aluno =  input('Segundo aluno: ')
terceiro_aluno =  input('Terceiro aluno: ')
quarto_aluno =  input('Quarto aluno: ')
lista_alunos = [primeiro_aluno, segundo_aluno, terceiro_aluno, quarto_aluno]
ordem_alunos = sample(lista_alunos, len(lista_alunos))
print(f'A ordem de apresentação será {ordem_alunos}')
