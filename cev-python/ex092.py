from datetime import date

trabalhador = {}

trabalhador['nome'] = input('Nome: ').strip().capitalize()
trabalhador['idade'] = date.today().year - int(input('Ano de nascimento: '))
trabalhador['ctps'] = int(input('Carteira de Trabalho (0 não tem): '))
if trabalhador['ctps'] != 0:
    trabalhador['contratação'] = int(input('Ano de contratação: '))
    trabalhador['salário'] = float(input('Salário: '))
    trabalhador['aposentadoria'] = trabalhador['idade'] + ((trabalhador['contratação'] + 35) - date.today().year) 
print('-='*20)

for k, v in trabalhador.items():
    print(f'- {k} tem o valor {v}')