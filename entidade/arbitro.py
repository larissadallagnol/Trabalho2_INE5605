# Entidade Arbitro

from entidade.abstractPessoa import AbstractPessoa
import datetime

class Arbitro(AbstractPessoa):
    def __init__(self, nome: str, cpf :str, data_de_nascimento: datetime.date, numero_partidas: int):
        super().__init__(nome, cpf, data_de_nascimento)
        self.__numero_partidas = numero_partidas
    
    @property
    def numero_partidas(self):
        return self.__numero_partidas
    
    @numero_partidas.setter
    def numero_partidas(self, numero_partidas):
        self.__numero_partidas = numero_partidas
