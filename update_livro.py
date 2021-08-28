import sqlite3

def editar_livro(id): #Edição do livre já cadastrado na base de dados
    try:
        con = sqlite3.connect('livros.db')
        cursor = con.cursor()
        #Checar se o ID do livro existe
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
editar_livro(1)