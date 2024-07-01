from persistencia.dao import DAO
from entidade.curso import Curso

class CursoDAO(DAO):
    def __init__(self):
        super().__init__('curso.pkl')

    def add(self, curso: Curso):
        if isinstance(curso, Curso):
            super().add(curso.codigo, curso)

    def remove(self, curso: Curso):
        if isinstance(curso, Curso):
            super().remove(curso.codigo)
