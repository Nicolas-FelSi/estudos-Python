pessoa = {}
pessoas = []
media_idade = 0
soma_idade = 0 

while True:
    pessoa['nome'] = input('Nome: ').strip().capitalize()
    
    pessoa['sexo'] = ' '
    while pessoa['sexo'] not in 'MF':      
        pessoa['sexo'] = input('Sexo: [M/F] ').strip().upper()
        if pessoa['sexo'] not in 'MF':
            print('ERRO! Por favor, digite apenas M ou F.')
            
    pessoa['idade'] = int(input('Idade: '))
    
    continuar = ' '
    while continuar not in 'SN':
        continuar = input('Quer continuar? [S/N] ').strip().upper()
        if continuar not in 'SN':
            print('ERRO! Por favor, digite apenas S ou N.')
    
    pessoas.append(pessoa.copy())
    
    if continuar == 'N':
        break
    
for pessoa in pessoas:
    if pessoa['idade'] :
        soma_idade += pessoa['idade']
media_idade = soma_idade/len(pessoas)
print('-='*30)
print(f'A) Ao todo temos {len(pessoas)} pessoas cadastradas.')
print(f'B) A média de idade é de {media_idade} anos.')
print(f'C) As mulheres cadastradas foram', end=' ')
for pessoa in pessoas:
    if pessoa['sexo'] == 'F':
        print(pessoa['nome'], end=' ')
                
print(f'\nD) Lista das pessoas que estão acima da média: ')
for pessoa in pessoas:
    if pessoa['idade'] > media_idade:
        for k, v in pessoa.items():
            print(f'{k} = {v};', end=' ')
        print()