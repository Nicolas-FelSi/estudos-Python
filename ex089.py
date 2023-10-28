alunos = []
aluno = []

while True:
    aluno.append(str(input('Nome: ').strip().title()))
    aluno.append(float(input('Nota 1: ')))
    aluno.append(float(input('Nota 2: ')))
    alunos.append(aluno.copy())
    aluno.clear()
    
    continuar = ' '
    while continuar not in 'SN':
        continuar = input('Quer continuar? [S/N] ').strip().upper()
    
    if continuar == 'N':
        break

print('-='*30)
print('Nº{:>4}NOME{:>10}MÉDIA'.format(' ', ' '))
print('-'*30)
for pos, aluno in enumerate(alunos):
    media = (aluno[1] + aluno[2])/2
    print(f'{pos:<6}{aluno[0]:<14}{media}')  
print('-'*30)

while True:
    mostrar_nota = int(input('Mostrar notas de qual aluno? (999 interrompe): '))
    
    if mostrar_nota == 999:
        break

    for pos, aluno in enumerate(alunos):
        if mostrar_nota == pos:
            print(f'Notas de {aluno[0]} são [{aluno[1]}, {aluno[2]}]')
            
    print('-'*30)
 