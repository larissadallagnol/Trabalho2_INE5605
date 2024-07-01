# Controlador geral do sistema

from limite.telaSistema import TelaSistema
from controle.controladorAluno import ControladorAluno
from controle.controladorArbitro import ControladorArbitro
from controle.controladorCurso import ControladorCurso
from controle.controladorEquipe import ControladorEquipe
from controle.controladorPartida import ControladorPartida
from controle.controladorCampeonato import ControladorCampeonato

class ControladorSistema:
    def __init__(self):
        self.__controlador_aluno = ControladorAluno(self)
        self.__controlador_arbitro = ControladorArbitro(self)
        self.__controlador_curso = ControladorCurso(self)
        self.__controlador_equipe = ControladorEquipe(self)
        self.__controlador_partida = ControladorPartida(self)
        self.__controlador_campeonato = ControladorCampeonato(self)
        self.__tela_sistema = TelaSistema()

    @property
    def controlador_aluno(self):
        return self.__controlador_aluno

    @property
    def controlador_arbitro(self):
        return self.__controlador_arbitro

    @property
    def controlador_curso(self):
        return self.__controlador_curso

    @property
    def controlador_equipe(self):
        return self.__controlador_equipe

    @property
    def controlador_partida(self):
        return self.__controlador_partida

    @property
    def controlador_campeonato(self):
        return self.__controlador_campeonato
    
    def gerar_relatorio_ganhadores(self):
        print("Classificacao do campeonato:")
        print(self.cadastra_campeonatos.classificacao())
        print("A equipe ganhadora do campeonato é a: ")
    
    def gerar_relatorio_equipe_fez_mais_gols(self):
        return
    
    def gerar_relatorio_equipe_levou_mais_gols(self):
        return
    
    def gerar_relatorio_jogadores_mais_gols(self):
        return

    def iniciar_sistema(self):
        self.abre_tela()

    def cadastra_alunos(self):
        self.__controlador_aluno.abre_tela()

    def cadastra_arbitros(self):
        self.__controlador_arbitro.abre_tela()

    def cadastra_cursos(self):
        self.__controlador_curso.abre_tela()

    def cadastra_equipes(self):
        self.__controlador_equipe.abre_tela()

    def cadastra_partidas(self):
        self.__controlador_partida.abre_tela()

    def cadastra_campeonatos(self):
        self.__controlador_campeonato.abre_tela()

    def encerra_sistema(self):
        exit(0)

    def abre_tela(self):
        lista_opcoes = {1: self.cadastra_cursos, 2: self.cadastra_alunos, 3: self.cadastra_arbitros, 4: self.cadastra_equipes, 
                        5: self.cadastra_partidas, 6: self.cadastra_campeonatos, 0: self.encerra_sistema}

        while True:
            opcao_escolhida = self.__tela_sistema.tela_opcoes()
            funcao_escolhida = lista_opcoes[opcao_escolhida]
            funcao_escolhida()
