# Entidade Aluno

from entidade.abstractPessoa import AbstractPessoa
from entidade.curso import Curso
import datetime

class Aluno(AbstractPessoa):
    def __init__(self, nome: str, cpf :int, data_de_nascimento: datetime.date, matricula: str, curso: Curso):
        super().__init__(nome, cpf, data_de_nascimento)
        self.__matricula = matricula
        self.__curso = curso

    @property
    def matricula(self):
        return self.__matricula

    @property
    def curso(self):
        return self.__curso

    @matricula.setter
    def matricula(self, matricula):
        self.__matricula = matricula

    @curso.setter
    def curso(self, curso):
        self.__curso = curso
