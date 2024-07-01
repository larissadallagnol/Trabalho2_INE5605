# Entidade Equipe

from entidade.curso import Curso

class Equipe():
    def __init__(self, nome: str, curso: Curso, lista_alunos: list, pontos: int, saldo_de_gols: int):
        self.__nome = nome
        self.__curso = curso
        self.__lista_alunos = lista_alunos
        self.__pontos : pontos = 0
        self.__saldo_de_gols : saldo_de_gols = 0
    
    @property
    def nome(self):
        return self.__nome

    @property
    def curso(self):
        return self.__curso

    @property
    def lista_alunos(self):
        return self.__lista_alunos

    @property
    def pontos(self):
        return self.__pontos

    @property
    def saldo_de_gols(self):
        return self.__saldo_de_gols
    
    @nome.setter
    def nome(self, nome):
        self.__nome = nome
    
    @curso.setter
    def curso(self, curso):
        self.__curso = curso
    
    @lista_alunos.setter
    def lista_alunos(self, lista_alunos):
        self.__lista_alunos = lista_alunos
    
    @pontos.setter
    def pontos(self, pontos):
        self.__pontos = pontos

    @saldo_de_gols.setter
    def saldo_de_gols(self, saldo_de_gols):
        self.__saldo_de_gols = saldo_de_gols
