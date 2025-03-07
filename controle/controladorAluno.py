# Controlador Aluno

from entidade.aluno import Aluno
from limite.telaAluno import TelaAluno
from persistencia.alunoDAO import AlunoDAO
from datetime import datetime

class ControladorAluno():
    def __init__(self, controlador_sistema):
        self.__tela_aluno = TelaAluno()
        self.__aluno_dao = AlunoDAO()
        self.__controlador_sistema = controlador_sistema

    @property
    def alunos(self):
        return self.__aluno_dao

    # Busca um aluno pelo CPF dele
    def busca_aluno_por_cpf(self, cpf: str):
        for aluno in self.__aluno_dao.get_all():
            if aluno.cpf == cpf:
                return aluno
        else:
            self.__tela_aluno.mostra_mensagem("ATENCAO: Este aluno nao existe!")
        return None

    # Cadastra um aluno novo
    def cadastrar_aluno(self):
        dados_aluno = self.__tela_aluno.pega_dados_aluno()
        existe_aluno = False
        for aluno in self.__aluno_dao.get_all():
            if aluno.cpf == dados_aluno["cpf"]:
                existe_aluno = True
        if existe_aluno is False:
            curso = self.__controlador_sistema.controlador_curso.busca_curso_por_codigo(dados_aluno["curso"])
            if curso is not None:
                data = datetime.strptime(dados_aluno["data_de_nascimento"], "%d/%m/%Y")
                novo_aluno = Aluno(dados_aluno["nome"], dados_aluno["cpf"], data.date(), 
                                dados_aluno["matricula"], curso.nome)
                self.__aluno_dao.add(novo_aluno)
                self.__tela_aluno.mostra_mensagem("Aluno cadastrado com sucesso!")
            else:
                self.__tela_aluno.mostra_mensagem("ATENCAO: Curso nao existe!")
        else:
            self.__tela_aluno.mostra_mensagem("ATENCAO: Aluno ja existente!")

    # Edita um aluno existente
    def editar_aluno(self):
        if len(self.__aluno_dao.get_all()) != 0:
            cpf_aluno = self.__tela_aluno.seleciona_aluno()
            aluno = self.busca_aluno_por_cpf(cpf_aluno)

            if aluno is not None:
                novos_dados_aluno = self.__tela_aluno.pega_dados_aluno()
                curso = self.__controlador_sistema.controlador_curso.busca_curso_por_codigo(novos_dados_aluno["curso"])
                if curso is not None:
                    aluno.nome = novos_dados_aluno["nome"]
                    aluno.cpf = novos_dados_aluno["cpf"]
                    data = datetime.strptime(novos_dados_aluno["data_de_nascimento"], "%d/%m/%Y")
                    aluno.data_de_nascimento = data.date()
                    aluno.matricula = novos_dados_aluno["matricula"]
                    aluno.curso = curso.nome
                    self.__aluno_dao.update(aluno)
                    self.__tela_aluno.mostra_mensagem("Aluno editado com sucesso!")
                else:
                    self.__tela_aluno.mostra_mensagem("ATENCAO: Curso nao existe!")
            else:
                self.__tela_aluno.mostra_mensagem("ATENCAO: Este aluno nao existe!")

    # Exclui um aluno existente
    def excluir_aluno(self):
        if len(self.__aluno_dao.get_all()) != 0:
            cpf_aluno = self.__tela_aluno.seleciona_aluno()
            aluno = self.busca_aluno_por_cpf(cpf_aluno)

            if aluno is not None:
                self.__aluno_dao.remove(aluno)
                self.__tela_aluno.mostra_mensagem("Aluno excluido com sucesso!")
            else:
                self.__tela_aluno.mostra_mensagem("ATENCAO: Este aluno nao existe!")

    # Lista os alunos existentes
    def listar_alunos(self):
        if len(self.__aluno_dao.get_all()) != 0:
            self.__tela_aluno.mostra_mensagem("Alunos cadastrados:")
            for aluno in self.__aluno_dao.get_all():
                self.__tela_aluno.mostra_aluno({"nome": aluno.nome, "cpf": aluno.cpf, "data_de_nascimento": aluno.data_de_nascimento, 
                                                "matricula": aluno.matricula, "curso": aluno.curso})
        else:
            self.__tela_aluno.mostra_mensagem("ATENCAO: Ainda nao existem alunos!")

    # Finaliza o uso do controlador e volta para o sistema principal
    def finalizar(self):
        self.__controlador_sistema.abre_tela()

    # Abre tela de opcoes
    def abre_tela(self):
        lista_opcoes = {0: self.finalizar, 1: self.cadastrar_aluno, 2: self.editar_aluno, 
                        3: self.excluir_aluno, 4: self.listar_alunos}
        while True:
            lista_opcoes[self.__tela_aluno.tela_opcoes()]()
