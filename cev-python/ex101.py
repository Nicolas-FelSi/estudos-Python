def voto(ano_nasc):
    from datetime import date
    idade = date.today().year - ano_nasc
    if idade > 0 and idade < 16:
        return print(f'Com {idade} anos: NÃO VOTA.')
    elif idade == 16 or idade == 17 or idade >= 65:
        return print(f'Com {idade} anos: VOTO OPCIONAL.')
    elif idade >= 18:
        return print(f'Com {idade} anos: VOTO OBRIGATÓRIO.')
    else:
        return print()


print('-'*30)
ano_nasc = int(input('Em que ano você nasceu? '))
voto(ano_nasc)
