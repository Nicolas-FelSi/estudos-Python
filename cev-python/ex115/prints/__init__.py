def linhas():
    print('-'*30)
    
def menu():
    linhas()
    print('{:>7}MENU PRINCIPAL'.format(' '))
    linhas()
    print('\033[1;33m1\033[m - \033[34mVer pessoas cadastradas\033[m')
    print('\033[1;33m2\033[m - \033[34mCadastrar nova Pessoa\033[m')
    print('\033[1;33m3\033[m - \033[34mSair do Sistema\033[m')
    linhas()
