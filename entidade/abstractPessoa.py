# classe abstrata - Pessoa

from abc import ABC, abstractmethod
import datetime

class AbstractPessoa(ABC):
    @abstractmethod
    def __init__(self, nome: str, cpf: int, data_de_nascimento: datetime.date):
        self.__nome = nome
        self.__cpf = cpf
        self.__data_de_nascimento = data_de_nascimento

    @property
    def nome(self) -> str:
        return self.__nome

    @property
    def cpf(self) -> str:
        return self.__cpf

    @property
    def data_de_nascimento(self) -> datetime.date:
        return self.__data_de_nascimento

    @nome.setter
    def nome(self, nome):
        self.__nome = nome

    @cpf.setter
    def cpf(self, cpf):
        self.__cpf = cpf

    @data_de_nascimento.setter
    def data_de_nascimento(self, data_de_nascimento):
        self.__data_de_nascimento = data_de_nascimento
