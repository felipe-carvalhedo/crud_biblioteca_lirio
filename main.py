from classe_livro import *
from crud import *
from nova_tabela_livros import criar_tabela


def menu(): #Menu de escolhas do programa
    criar_tabela()
    while True:
        opcao_menu = input("\nSeja Bem-vindo ao Menu da Lírio Livros! O que deseja fazer?\n1 - "\
            "Cadastrar um novo livro.\n2 - Deletar um livro cadastrado.\n3 - Editar um"\
            "livro cadastrado.\n4 - Listar livros cadastrados.\n5 - Resetar tabela.\n6 - Finalizar programa.\n\n")
        try:
            opcao_menu = int(opcao_menu)
        except TypeError:
            print("Você digitou uma opção incorreta, por favor digite uma opção de menu de 1 a 5.")
        except ValueError:
            print("Você digitou uma opção incorreta, por favor digite uma opção de menu de 1 a 5.")
        if opcao_menu == 1:
            while True:
                continuar = input("Deseja adicionar outro livro? S para sim e N para não.\n").upper()
                if continuar == 'N':
                    break
                elif continuar == 'S':
                    nome_livro = input("Digite o nome do livro que deseja cadastrar.\n")
                    nome_autor = input("Digite o nome do autor do livro.\n")
                    quantidade_paginas = input("Digite a quantidade de páginas do livro.\n")
                    preco_livro = input("Digite o valor do livro.\n")
                    insert_livro(nome_livro,nome_autor, quantidade_paginas, preco_livro)
                else:
                    print("Opção inválida.\n")
            print()
        elif opcao_menu == 2:
            numero_id = input("Digite o id do livro que deseja remover: ")
            delete_livro(numero_id)
            print()
        elif opcao_menu == 3:
            numero_id = input("Digite o id do livro que deseja editar: ")
            editar_livro(numero_id)
            print()
        elif opcao_menu == 4:
            while True:
                pesquisa_por_livro = input("Escolha '1' para buscar um livro e '2' para listar todos os livros: ")
                if pesquisa_por_livro == '1':
                    livro_id = input("Digite o id do livro que deseja buscar: ")
                    mostrar_livro(livro_id)
                    break
                elif pesquisa_por_livro == '2':
                    mostrar_todos_livros()
                    break
                else:
                    print("Você digitou uma opção inválida.\n")
        elif opcao_menu == 5:
            reset_tabela()
        elif opcao_menu == 6:
            print()
            print("Programa finalizado.\n")
            break
        else:
            print("Você digitou uma opção inválida, por favor tente novamente com uma opção válida!\n")
            print()
            continue

#Programa principal
opcao_escolhida = menu()