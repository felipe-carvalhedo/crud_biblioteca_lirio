import sqlite3

def criar_tabela(): #Cria uma tabela para armazenar os livros caso a tabela ainda não exista
    con = sqlite3.connect('livros.db')
    cursor = con.cursor()
    cursor.execute('CREATE TABLE IF NOT EXISTS Livros(''id INTEGER PRIMARY KEY AUTOINCREMENT,'
                                            'nome TEXT NOT NULL,''autor TEXT NOT NULL,'
                                            'paginas INTEGER NOT NULL,' 'preco REAL NOT NULL'')')
    
    con.commit()
    con.close()