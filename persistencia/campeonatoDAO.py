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

    def update(self, campeonato: Campeonato):
        if isinstance(campeonato, Campeonato):
            for key, obj in self._DAO__cache.items():
                if isinstance(obj, Campeonato) and obj.nome == campeonato.nome:
                    super().update(key, campeonato)
                    return
            print(f"Campeonato de nome {campeonato.nome} não encontrado no cache.")
