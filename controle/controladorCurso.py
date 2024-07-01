# Controlador Curso

from entidade.curso import Curso
from limite.telaCurso import TelaCurso
from persistencia.cursoDAO import CursoDAO

class ControladorCurso():
    def __init__(self, controlador_sistema):
        self.__tela_curso = TelaCurso()
        self.__curso_dao = CursoDAO()
        self.__controlador_sistema = controlador_sistema
    
    @property
    def cursos(self):
        return self.__curso_dao.get_all()

    # Busca um curso pelo seu codigo
    def busca_curso_por_codigo(self, codigo: int):
        for curso in self.__curso_dao.get_all():
            if curso.codigo == codigo:
                return curso
        else:
            self.__tela_curso.mostra_mensagem("Curso pesquisado pode estar errado ou nao existe!")
        return None

    # Verifica se algum curso esta sem equipe
    def verifica_cursos_sem_equipe(self):
        for curso in self.__curso_dao.get_all():
            if curso.equipes == []:
                print("ATENCAO: O curso {} está sem equipes!".format(curso.nome))
                print("Crie ao menos uma equipe para cada curso!")

    # Cadastra um curso novo
    def cadastrar_curso(self):
        dados_curso = self.__tela_curso.pega_dados_curso()
        existe_curso = False
        for curso in self.__curso_dao.get_all():
            if curso.codigo == dados_curso["codigo"]:
                existe_curso = True
        if existe_curso is False:
            novo_curso = Curso(dados_curso["codigo"], dados_curso["nome"], dados_curso["equipes"])
            self.__curso_dao.add(novo_curso)
            self.__tela_curso.mostra_mensagem("Curso cadastrado com sucesso!")
        else:
            self.__tela_curso.mostra_mensagem("ATENCAO: Curso ja existente!")

    # Edita um curso existente
    def editar_curso(self):
        if len(self.__curso_dao.get_all()) != 0:
            codigo_curso = self.__tela_curso.seleciona_curso()
            curso = self.busca_curso_por_codigo(codigo_curso)

            if curso is not None:
                novos_dados_curso = self.__tela_curso.pega_dados_curso()
                for aluno in self.__controlador_sistema.controlador_aluno.alunos.get_all():
                    if aluno.curso == curso.nome:
                        aluno.curso = novos_dados_curso["nome"]
                        self.__controlador_sistema.controlador_aluno.alunos.update(aluno)
                curso.codigo = novos_dados_curso["codigo"]
                curso.nome = novos_dados_curso["nome"]
                curso.equipes = novos_dados_curso["equipes"]
                self.__curso_dao.update(curso)
                self.__tela_curso.mostra_mensagem("Curso editado com sucesso!")
            else:
                self.__tela_curso.mostra_mensagem("ATENCAO: Este curso nao existe!")

    # Exclui um curso existente
    def excluir_curso(self):
        if len(self.__curso_dao.get_all()) != 0:
            codigo_curso = self.__tela_curso.seleciona_curso()
            curso = self.busca_curso_por_codigo(codigo_curso)

            if curso is not None:
                self.__curso_dao.remove(curso)
                self.__tela_curso.mostra_mensagem("Curso excluido com sucesso!")
            else:
                self.__tela_curso.mostra_mensagem("ATENCAO: Este curso nao existe!")

    # Lista os cursos existentes
    def listar_cursos(self):
        if len(self.__curso_dao.get_all()) != 0:
            self.__tela_curso.mostra_mensagem("Cursos cadastrados:")
            for curso in self.__curso_dao.get_all():
                self.__tela_curso.mostra_curso({"codigo": curso.codigo, "nome": curso.nome, "equipes": curso.equipes})
        else:
            self.__tela_curso.mostra_mensagem("ATENCAO: Ainda nao existem cursos!")

    # Finaliza o uso do controlador e volta para o sistema principal
    def finalizar(self):
        self.__controlador_sistema.abre_tela()

    # Abre tela de opcoes 
    def abre_tela(self):
        lista_opcoes = {0: self.finalizar, 1: self.cadastrar_curso, 2: self.editar_curso, 
                        3: self.excluir_curso, 4: self.listar_cursos}
        while True:
            lista_opcoes[self.__tela_curso.tela_opcoes()]()
