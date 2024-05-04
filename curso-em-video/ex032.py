from datetime import datetime

ano = int(input("Que ano quer analisar? Coloque 0 para analisar o ano atual: "))

if ano == 0:
    ano = datetime.now().year

if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print(f"O ano {ano} é bissexto (tem 366 dias).")
else:
    print(f"O ano {ano} não é um ano bissexto (tem 365 dias).")
    