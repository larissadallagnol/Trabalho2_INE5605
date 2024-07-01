# Controlador Equipe

from entidade.equipe import Equipe
from limite.telaEquipe import TelaEquipe

class ControladorEquipe():
    def __init__(self, controlador_sistema):
        self.__tela_equipe = TelaEquipe()
        self.__equipes = []
        self.__controlador_sistema = controlador_sistema

    @property
    def equipes(self):
        return self.__equipes

    # Busca uma equipe pelo nome dela
    def busca_equipe_por_nome(self, nome: str):
        for equipe in self.__equipes:
            if equipe.nome == nome:
                return equipe
        return None

    # Cadastra uma equipe nova
    def cadastrar_equipe(self):
        dados_equipe = self.__tela_equipe.pega_dados_equipe()
        existe_equipe = False
        for equipe in self.__equipes:
            if equipe.nome == dados_equipe["nome"]:
                existe_equipe = True
        if existe_equipe is False:
            curso_equipe = self.__controlador_sistema.controlador_curso.busca_curso_por_codigo(dados_equipe["curso"])
            cpf_split = dados_equipe["lista_alunos"].split()
            alunos_equipe = []
            for cpf in cpf_split:
                aluno = self.__controlador_sistema.controlador_aluno.busca_aluno_por_cpf(int(cpf))
                if aluno.curso == curso_equipe.nome:
                    alunos_equipe.append(aluno.nome)
                else:
                    print("ATENCAO: Este aluno nao pertence ao curso da equipe!") 
            nova_equipe = Equipe(dados_equipe["nome"], curso_equipe.nome, alunos_equipe, dados_equipe["pontos"], dados_equipe["saldo_de_gols"])
            self.__equipes.append(nova_equipe)
            for curso in self.__controlador_sistema.controlador_curso.cursos:
                if curso.nome == curso_equipe.nome:
                    curso.equipes.append(nova_equipe.nome)
            self.__controlador_sistema.controlador_curso.verifica_cursos_sem_equipe()
        else:
            self.__tela_equipe.mostra_mensagem("ATENCAO: Equipe ja existente!")

    # Edita uma equipe existente
    def editar_equipe(self):
        self.listar_equipes()
        nome_equipe = self.__tela_equipe.seleciona_equipe()
        equipe = self.busca_equipe_por_nome(nome_equipe)

        if equipe is not None:
            novos_dados_equipe = self.__tela_equipe.pega_dados_equipe()
            equipe.nome = novos_dados_equipe["nome"]
            curso = self.__controlador_sistema.controlador_curso.busca_curso_por_codigo(novos_dados_equipe["curso"])
            equipe.curso = curso.nome
            alunos_equipe = []
            cpf_split = novos_dados_equipe["lista_alunos"].split()
            for cpf in cpf_split:
                aluno = self.__controlador_sistema.controlador_aluno.busca_aluno_por_cpf(int(cpf))
                # iserir tratamento caso o aluno nao existir
                if aluno.curso == curso.nome:
                    alunos_equipe.append(aluno.nome)
                else:
                    print("ATENCAO: Este aluno nao pertence ao curso da equipe!")
            equipe.lista_alunos = alunos_equipe
            self.listar_equipes()
        else:
            self.__tela_equipe.mostra_mensagem("ATENCAO: Esta equipe nao existe!")

    # Exclui uma equipe existente
    def excluir_equipe(self):
        self.listar_equipes()
        nome_equipe = self.__tela_equipe.seleciona_equipe()
        equipe = self.busca_equipe_por_nome(nome_equipe)

        if equipe is not None:
            self.__equipes.remove(equipe)
            self.__tela_equipe.mostra_mensagem("Equipe excluida!")
            for curso in self.__controlador_sistema.controlador_curso.cursos:
                if curso == equipe.curso:
                    curso.equipes.remove(equipe)
                    self.__tela_equipe.mostra_mensagem("Equipe excluida da lista de equipes do curso!")
        else:
            self.__tela_equipe.mostra_mensagem("ATENCAO: Esta equipe nao existe!")

    # Lista as equipes existentes
    def listar_equipes(self):
        if len(self.__equipes) != 0:
            self.__tela_equipe.mostra_mensagem("Equipes cadastradas:")
            for equipe in self.__equipes:
                self.__tela_equipe.mostra_equipe({"nome": equipe.nome, "curso": equipe.curso, 
                                              "lista_alunos": equipe.lista_alunos, "pontos": equipe.pontos, "saldo_de_gols": equipe.saldo_de_gols})
        else:
            self.__tela_equipe.mostra_mensagem("ATENCAO: Ainda nao existem equipes!")

    # Finaliza o uso do controlador e volta para o sistema principal
    def finalizar(self):
        self.__controlador_sistema.abre_tela()

    # Abre tela de opcoes
    def abre_tela(self):
        lista_opcoes = {0: self.finalizar, 1: self.cadastrar_equipe, 2: self.editar_equipe, 
                        3: self.excluir_equipe, 4: self.listar_equipes}
        while True:
            lista_opcoes[self.__tela_equipe.mostra_tela_opcoes()]()
