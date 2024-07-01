# Entidade Curso

class Curso():
    def __init__(self, codigo: int, nome: str, equipes: list):
        self.__codigo = codigo
        self.__nome = nome
        self.__equipes = equipes
    
    @property
    def codigo(self):
        return self.__codigo
    
    @property
    def nome(self):
        return self.__nome

    @property
    def equipes(self):
        return self.__equipes

    @codigo.setter
    def codigo(self, codigo):
        self.__codigo = codigo
    
    @nome.setter
    def nome(self, nome):
        self.__nome = nome
    
    @equipes.setter
    def equipes(self, equipes):
        self.__equipes = equipes
