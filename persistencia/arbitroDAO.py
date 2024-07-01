from persistencia.dao import DAO
from entidade.arbitro import Arbitro

class ArbitroDAO(DAO):
    def __init__(self):
        super().__init__('arbitro.pkl')

    def add(self, arbitro: Arbitro):
        if isinstance(arbitro, Arbitro):
            super().add(arbitro.cpf, arbitro)

    def remove(self, arbitro: Arbitro):
        if isinstance(arbitro, Arbitro):
            super().remove(arbitro.cpf)

    def update(self, arbitro: Arbitro):
        if isinstance(arbitro, Arbitro):
            for key, obj in self._DAO__cache.items():
                if isinstance(obj, Arbitro) and obj.cpf == arbitro.cpf:
                    super().update(key, arbitro)
                    return
            print(f"Arbitro com CPF {arbitro.cpf} não encontrado no cache.")
