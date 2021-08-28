import sqlite3

def delete_livro(id): #Deletar um livro cadastrado na base de dados
    try:
        con = sqlite3.connect('livros.db')
        cursor = con.cursor()
        try:
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
