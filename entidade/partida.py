# Entidade Partida

from entidade.equipe import Equipe
from entidade.arbitro import Arbitro
import datetime

class Partida():
    def __init__(self, numero: int, data: datetime.date, primeira_equipe: Equipe, segunda_equipe: Equipe, 
                 arbitro: Arbitro, gols_primeira_equipe: int, gols_segunda_equipe: int):
        self.__numero = numero
        self.__data = data
        self.__primeira_equipe = primeira_equipe
        self.__segunda_equipe = segunda_equipe
        self.__arbitro = arbitro
        self.__gols_primeira_equipe = gols_primeira_equipe
        self.__gols_segunda_equipe = gols_segunda_equipe
    
    @property
    def numero(self):
        return self.__numero

    @property
    def data(self):
        return self.__data

    @property
    def primeira_equipe(self):
        return self.__primeira_equipe

    @property
    def segunda_equipe(self):
        return self.__segunda_equipe

    @property
    def arbitro(self):
        return self.__arbitro

    @property
    def gols_primeira_equipe(self):
        return self.__gols_primeira_equipe

    @property
    def gols_segunda_equipe(self):
        return self.__gols_segunda_equipe
    
    @numero.setter
    def numero(self, numero):
        self.__numero = numero
    
    @data.setter
    def data(self, data):
        self.__data = data
    
    @primeira_equipe.setter
    def primeira_equipe(self, primeira_equipe):
        self.__primeira_equipe = primeira_equipe
    
    @segunda_equipe.setter
    def segunda_equipe(self, segunda_equipe):
        self.__segunda_equipe = segunda_equipe
    
    @arbitro.setter
    def arbitro(self, arbitro):
        self.__arbitro = arbitro
    
    @gols_primeira_equipe.setter
    def gols_primeira_equipe(self, gols_primeira_equipe):
        self.__gols_primeira_equipe = gols_primeira_equipe
    
    @gols_segunda_equipe.setter
    def gols_segunda_equipe(self, gols_segunda_equipe):
        self.__gols_segunda_equipe = gols_segunda_equipe
