import sqlite3

#Inserção de novo livro.
def insert_livro(nome, autor, paginas, preco):
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

#Remoção de livro.
def delete_livro(id):
    try:
        con = sqlite3.connect('livros.db')
        cursor = con.cursor()
        try:
            cursor.execute(f'SELECT * FROM Livros WHERE id="{id}"')
            record_id = cursor.fetchone()
            if not record_id:
                return print("\nO id informado não existe.")
            cursor.execute('DELETE FROM Livros WHERE id=:id', {'id': id})   
            con.commit()
            con.close()
        except ValueError as error:
            return print("Não foi possível acessar o id informado, por favor tente um id válido.")
    except sqlite3.Error as error:
        return print("Não foi possível ler a base de dados.", error)
    finally:
        if con:
            con.close()

#Edição de livro já adicionado.
def editar_livro(id):
    try:
        con = sqlite3.connect('livros.db')
        cursor = con.cursor()
        #CHECAR SE O ID EXISTE
        cursor.execute(f'SELECT id FROM Livros WHERE id="{id}"')
        record_id = cursor.fetchone()
        if not record_id:
            return print("Não é possível editar um livro que ainda não foi cadastrado.")
        try: #Checar se o nome informado já existe na base de dados.
            novo_nome = input("Digite o novo nome para o livro: ")
            cursor.execute(f'SELECT * FROM Livros WHERE nome="{novo_nome}"')
            record_novo_nome = cursor.fetchone()
            if record_novo_nome:
                return print("Já existe um livro cadastrado com esse nome e o sistema não aceita duplicata.")
        except TypeError:
            return print("Algo deu errado ao verificar novo nome e novo autor.")
        try: #Checar se o autor informado já existe na base de dados.
            novo_autor = input("Digite o novo autor para o livro: ")
            cursor.execute(f'SELECT * FROM Livros WHERE autor="{novo_autor}"')
            record_novo_autor = cursor.fetchone()
            if record_novo_autor:
                return print("Já existe um autor cadastrado com esse nome e o sistema não aceita duplicata.")
        except TypeError:
            return print("Algo deu errado ao verificar novo nome e novo autor.")
        try: #Checar se a quantidade de páginas informada é maior do que 0.
            nova_qta_pagina = input("Digite uma nova quantidade de páginas para o livro: ")
            nova_qta_pagina = int(nova_qta_pagina)
            if nova_qta_pagina <= 0:
                return print("Você não pode adicionar um livro que não possui páginas.")
        except ValueError as error:
            return print("O número de páginas informado precisa ser do tipo inteiro.", error)
        try: #Checar se o novo preço informado é maior do que 0. 
            novo_preco = input("Digite o novo preço para o livro: ")
            novo_preco = float(novo_preco)
            if novo_preco <= 0:
                return print("Valor inválido, por favor informe um valor maior do que 0.")
        except ValueError as error:
            return print("O valor informado precisa ser numérico.", error)
        cursor.execute('UPDATE Livros SET nome=:nome, autor=:autor, paginas=:paginas, preco=:preco WHERE id=:id',
        {'id': id,'nome': novo_nome, 'autor': novo_autor, 'paginas': nova_qta_pagina, 'preco': novo_preco})
        con.commit()
        con.close()
    except sqlite3.Error as error:
        print("Não foi possível ler os dados da tabela. As informações do livro não puderam ser modificadas.", error)
    finally:
        if con:
            con.close()

#Mostrar livros cadastrados.
def mostrar_todos_livros(): #Todos os livros
    try: 
        con = sqlite3.connect('livros.db')
        cursor = con.cursor()
        cursor.execute('SELECT * FROM Livros')
        records = cursor.fetchall()
        for row in records:
            print("Id: ", row[0])
            print("Nome: ", row[1])
            print("Autor: ", row[2])
            print("Páginas: ", row[3])
            print("Preço: ", row[4],"R$")
            print("\n")
        cursor.close()
    except sqlite3.Error as error:
        print("Não foi possível ler os dados da tabela", error)
    finally:
        if con:
            con.close()

def mostrar_livro(id): #Livro único passando o id.
    try:
        id = int(id)
    except ValueError:
        return print("O id informado é inválido, por favor escolha um id do tipo inteiro.")
    try: 
        con = sqlite3.connect('livros.db')
        cursor = con.cursor()
        cursor.execute(f'SELECT * from Livros WHERE id="{id}"')
        record_show_id = cursor.fetchone()
        if not record_show_id:
            return print("Não existe nenhum livro com ese id.")
        cursor.execute('SELECT id, nome, autor, paginas, preco FROM Livros WHERE id=:id',
                        {'id':id})
        record = cursor.fetchone()
        print("id: ", record[0])
        print("Nome: ", record[1])
        print("Autor: ", record[2])
        print("Páginas: ", record[3])
        print("Preço: ", record[4],"R$")
        print("\n")
        cursor.close()
        con.close()
    except sqlite3.Error as error:
        print("Não foi possível ler os dados da linha selecionada.", error)
    finally:
        if con:
            con.close()

#Resetar a tabela.
def reset_tabela():
    con = sqlite3.connect('livros.db')
    cursor = con.cursor()
    cursor.execute('DELETE FROM Livros')
    con.commit()
    cursor.close()
    con.close()