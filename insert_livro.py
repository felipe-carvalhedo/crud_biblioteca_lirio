import sqlite3

def insert_livro(nome, autor, paginas, preco): #Inserir novo livro na base de dados
    try: #Verificação do tipo de nome e autor.
        nome = str(nome)
        autor = str(autor)
    except TypeError as error:
        print("O tipo recebido precisa ser do tipo string.", error)
    try:
        paginas = int(paginas)
        if paginas <= 0:
            return print("A quantidade de páginas precisa ser maior do que 0")
    except ValueError as error:
        return print("A quantidade de páginas precisa ser do tipo inteiro.", error)
    try:
        preco = float(preco)
        if preco <= 0:
            return print("O preço do livro precisa ser maior do que 0.")
    except ValueError as error:
        return print("O valor precisa ser do tipo numérico.", error)
    try:
        con = sqlite3.connect('livros.db')
        cursor = con.cursor()
        cursor.execute(f'SELECT * FROM Livros WHERE nome="{nome}"')
        record_1 = cursor.fetchone()
        cursor.execute(f'SELECT * FROM Livros WHERE autor="{autor}"')
        record_2 = cursor.fetchone()
        if record_1 or record_2:
            print("Esse livro já foi cadastrado e o sistema não aceita duplicata.")
        else:
            cursor.execute(f'INSERT INTO Livros (nome, autor, paginas, preco) VALUES ("{nome}", "{autor}", {paginas}, {preco})')
        con.commit()
        con.close()
    except sqlite3.Error as error:
        print("Não foi possível ler os dados da tabela. O livro não pode ser adicionado", error)
    finally:
        if con:
            con.close()


