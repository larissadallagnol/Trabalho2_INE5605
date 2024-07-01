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
