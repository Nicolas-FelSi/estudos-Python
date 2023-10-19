from datetime import date
ano_digitado = int(input('Que ano quer analisar? Coloque 0 para analisar o ano atual: '))

if ano_digitado == 0:
    ano_digitado = date.today().year
if ano_digitado % 4 == 0 and ano_digitado % 100 != 0 or ano_digitado % 400 == 0:
    print(f'O ano {ano_digitado} é BISSEXTO')
else:
    print(f'O ano {ano_digitado} NÃO é BISSEXTO')