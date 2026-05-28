class jogo:
    def __init__(self,nome,genero,estoque,preco):
        self.__nome = nome
        self.__genero = genero
        self.__estoque = estoque
        self.__preco = preco

    def get_nome(self):
        return self.__nome
    def get_genero(self):
        return self.__genero
    def get_estoque(self):
        return self.__estoque
    def get_preco(self):
        return self.__preco



