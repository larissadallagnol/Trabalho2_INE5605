from persistencia.dao import DAO
from entidade.equipe import Equipe

class EquipeDAO(DAO):
    def __init__(self):
        super().__init__('equipe.pkl')

    def add(self, equipe: Equipe):
        if isinstance(equipe, Equipe):
            super().add(equipe.nome, equipe)

    def remove(self, equipe: Equipe):
        if isinstance(equipe, Equipe):
            super().remove(equipe.nome)

    def update(self, equipe: Equipe):
        if isinstance(equipe, Equipe):
            for key, obj in self._DAO__cache.items():
                if isinstance(obj, Equipe) and obj.nome == equipe.nome:
                    super().update(key, equipe)
                    return
            print(f"Equipe de nome {equipe.nome} não encontrado no cache.")
