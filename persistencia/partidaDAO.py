from persistencia.dao import DAO
from entidade.partida import Partida

class PartidaDAO(DAO):
    def __init__(self):
        super().__init__('partida.pkl')

    def add(self, partida: Partida):
        if isinstance(partida, Partida):
            super().add(partida.numero, partida)

    def remove(self, partida: Partida):
        if isinstance(partida, Partida):
            super().remove(partida.numero)
