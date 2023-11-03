from datetime import date

ano_nascimento = int(input('Ano nascimento: '))
ano_atual = date.today().year
idade = ano_atual - ano_nascimento

print(f'Quem nasceu em {ano_nascimento} tem {idade} anos em {ano_atual}.')

if idade < 18:
    anos_faltantes = 18-idade
    print(f'Ainda faltam {anos_faltantes} anos para o alistamento')
    print(f'Seu alistamento será em {ano_atual+anos_faltantes}')
elif idade == 18:
    print(f'Você tem que se alistar IMEDIATAMENTE!')
elif idade > 18:
    anos_passados = idade-18
    print(f'Você já deveria ter se alistado há {anos_passados} anos.')
    print(f'Seu alistamento foi em {ano_atual-anos_passados}')
else:
    print('Informação inválida. Tente novamente.')