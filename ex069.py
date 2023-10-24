maior_de_18 = 0
homens = 0
mulheres_menos_20 = 0

while True:
    print('-'*30)
    print('CADASTRE UMA PESSOA')
    print('-'*30)
    
    idade = int(input('Idade: '))
    sexo = ' '
    while sexo not in 'MF':
        sexo = input('Sexo: [M/F] ').strip().upper()
    print('-'*30)
    
    continuar = ' '
    while continuar not in 'SN':
        continuar = input('Quer continuar? [S/N] ').strip().upper()
        
    if idade >= 18:
        maior_de_18 += 1
    if sexo == 'M':
        homens += 1
    if sexo == 'F' and idade < 20:
        mulheres_menos_20 += 1
        
    if continuar == 'N':
        break 

print(f'Total de pessoas com mais de 18 anos: {maior_de_18}')
print(f'Ao todo temos {homens} homens cadastrados')
print(f'E temos {mulheres_menos_20} mulheres com menos de 20 anos')

    