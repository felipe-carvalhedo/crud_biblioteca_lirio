from datetime import datetime

class Livro: #Classe do objeto utilizado no programa

    def __init__(self, nome=None, autor=None, quantidade_paginas=None, preco=None):
        self.nome = nome
        self.autor = autor
        self.quantidade_paginas = quantidade_paginas
        self.preco = preco
        # self.data_inclusao = None
    
    @property
    def nome(self):
        return self._nome

    @property
    def autor(self):
        return self._autor

    @property
    def quantidade_paginas(self):
        return self._quantidade_paginas

    @property
    def preco(self):
        return self._preco

    @property
    def data_inclusao(self):
        return self._data_inclusao

    @nome.setter
    def nome(self, novo_nome):
        try: #Validação do nome do livro.
            novo_nome = str(novo_nome)
            self._nome = novo_nome
        except TypeError:
            print("Tipo de nome inválido, por favor tente novamente com um tipo de nome válido.")
        except ValueError:
            print("Nome inválido, por favor tente novamente com um nome válido.")


    @autor.setter
    def autor(self, novo_autor):
        try: #Validação do nome do autor
            novo_autor = str(novo_autor)
            self._autor = novo_autor
            len(novo_autor) > 0
        except TypeError:
            print("Tipo de autor inválido, por favor tente novamente com um tipo de autor válido.")
        except ValueError:
            print('Autor inválido, por favor tente novamente com um autor válido.')  

    @quantidade_paginas.setter
    def quantidade_paginas(self, nova_quantidade_paginas):
        try:    #Validação de quantidade de páginas            
            nova_quantidade_paginas = int(nova_quantidade_paginas)
            if nova_quantidade_paginas > 0:
                self._quantidade_paginas = nova_quantidade_paginas
        except TypeError:
            print("Tipo de quantidade de páginas precisa ser inteiro, por favor tente novamente.")
        except ValueError:
            print("O número de páginas precisa ser maior do que 0 e  precisa ser do tipo inteiro, por favor tente novamente.")   
        except AttributeError:
            print("Erro de atributo, por favor tente novamente")


    @preco.setter
    def preco(self, novo_preco):
        try: #Validação de preço
            novo_preco = float(novo_preco)
            if novo_preco > 0:
                self._preco = novo_preco
        except TypeError:
            print("Preco precisa ser do tipo flutuante, por favor tente novamente.")
        except ValueError:
            print("O valor para preço precisa ser maior do que 0, por favor tente novamente.")