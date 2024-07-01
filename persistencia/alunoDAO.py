from persistencia.dao import DAO
from entidade.aluno import Aluno

class AlunoDAO(DAO):
    def __init__(self):
        super().__init__('aluno.pkl')

    def add(self, aluno: Aluno):
        if isinstance(aluno, Aluno):
            super().add(aluno.cpf, aluno)

    def remove(self, aluno: Aluno):
        if isinstance(aluno, Aluno):
            super().remove(aluno.cpf)
