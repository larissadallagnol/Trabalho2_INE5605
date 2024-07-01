from persistencia.dao import DAO
from entidade.campeonato import Campeonato

class CampeonatoDAO(DAO):
    def __init__(self):
        super().__init__('campeonato.pkl')

    def add(self, campeonato: Campeonato):
        if isinstance(campeonato, Campeonato):
            super().add(campeonato.nome, campeonato)

    def remove(self, campeonato: Campeonato):
        if isinstance(campeonato, Campeonato):
            super().remove(campeonato.nome)
