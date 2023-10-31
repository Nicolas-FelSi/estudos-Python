def notas(*notas, situacao=False):
    '''
    --> Função para analisar notas e situações de vários alunos.
    :param n: uma ou mais notas dos alunos (aceita várias)
    :param sit: valor opcional, indicando se deve ou não adicionar a situação
    :return: dicionário com várias informações sobre a situação da turma.
    '''
    aluno = {}
    aluno['total'] = len(notas)
    aluno['maior'] = max(notas)
    aluno['menor'] = min(notas)
    aluno['média'] = sum(notas)/len(notas)
    if situacao:
        if aluno['média'] >= 7 and aluno['média'] <= 10:
            aluno['situação'] = 'BOA'
        elif aluno['média'] >= 5 and aluno['média'] < 7:
            aluno['situação'] = 'RAZOÁVEL'
        elif aluno['média'] >= 0 and aluno['média'] < 5:
            aluno['situação'] = 'RUIM'
    return aluno


resposta = notas(5.5, 9.5, 10, 6.5, situacao=True)
print(resposta)
help(notas)
