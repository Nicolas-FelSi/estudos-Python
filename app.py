import sqlite3


with sqlite3.connect('artistas.db') as conexao:
    sql = conexao.cursor()
    
    sql.execute('CREATE TABLE banda(nome text, estilo text, membros integer)')
    sql.execute('INSERT INTO banda(nome, estilo, membros) VALUES ("Banda 1", "Rock", 3)')
    
    nome = input('Digite o nome da banda: ').strip().title()
    estilo = input('Digite o estilo da banda: ').strip().title()
    quantidade_de_membros = int(input('Digite a quantidade de membros a banda: '))
    
    sql.execute('INSERT INTO banda VALUES(?, ?, ?)', [nome, estilo, quantidade_de_membros])
    
    conexao.commit()
    
    bandas = sql.execute('SELECT * FROM banda')
    
    for banda in bandas:
        print(banda)