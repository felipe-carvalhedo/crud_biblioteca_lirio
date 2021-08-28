import sqlite3

def mostrar_todos_livros(): #Mostra todos os livros cadastrados na base de dados
    try: 
        con = sqlite3.connect('livros.db')
        cursor = con.cursor()
        cursor.execute('SELECT * FROM Livros')
        records = cursor.fetchall()
        for row in records:
            print("Id ", row[0])
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


def mostrar_livro(id): #Mostra um livro cadastrado na base de dados através do ID do livro
    try: 
        con = sqlite3.connect('livros.db')
        cursor = con.cursor()
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
    except TypeError as error:
        print("Não foi possível ler os dados da linha selecionada.", error)
    finally:
        if con:
            con.close()

mostrar_todos_livros()
