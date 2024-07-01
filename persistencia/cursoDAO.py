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

    def update(self, curso: Curso):
        if isinstance(curso, Curso):
            for key, obj in self._DAO__cache.items():
                if isinstance(obj, Curso) and obj.codigo == curso.codigo:
                    super().update(key, curso)
                    return
            print(f"Curso com codigo {curso.codigo} não encontrado no cache.")
