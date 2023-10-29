aluno = {}
aluno['nome'] = str(input('Nome: ')).strip().title()
aluno['media'] = float(input(f'Média de {aluno["nome"]}: '))
print('-='*20)

for k, v in aluno.items():
    print(f'- {k} é igual a {v}')
    
if aluno['media'] >= 7 and aluno['media'] <= 10:
    print('- situação é igual a Aprovado')
elif aluno['media'] > 5 and aluno['media'] <= 6.9:
    print('- situação é igual a Recuperação')
elif aluno['media'] <= 5:
    print('- situação é igual a Reprovado')
else:
    print('- média inválida')