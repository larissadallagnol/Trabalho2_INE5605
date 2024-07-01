# Controlador Partida

from entidade.partida import Partida
from limite.telaPartida import TelaPartida
import datetime as dt
import random
from persistencia.partidaDAO import PartidaDAO

class ControladorPartida():
    def __init__(self, controlador_sistema):
        self.__tela_partida = TelaPartida()
        self.__partida_dao = PartidaDAO()
        self.__controlador_sistema = controlador_sistema
    
    @property
    def partidas(self):
        return self.__partida_dao.get_all()
    
    @partidas.setter
    def partidas(self, partidas):
        self.__partida_dao = partidas

    # Busca uma partida pelo numero dela
    def busca_partida_por_numero(self, numero: str):
        for partida in self.__partida_dao.get_all():
            if partida.numero == numero:
                return partida
        return None
    
    # Acrescenta pontos a uma equipe
    def acrescentar_pontos(self, partida: Partida):
        primeira_equipe = self.__controlador_sistema.controlador_equipe.busca_equipe_por_nome(partida.primeira_equipe)
        segunda_equipe = self.__controlador_sistema.controlador_equipe.busca_equipe_por_nome(partida.segunda_equipe)
        if partida.gols_primeira_equipe > partida.gols_segunda_equipe:
            primeira_equipe.pontos += 3
        elif partida.gols_primeira_equipe == partida.gols_segunda_equipe:
            primeira_equipe.pontos += 1
            segunda_equipe.pontos += 1
        else:
            segunda_equipe.pontos += 3

    # Descrementa pontos de uma equipe
    def decrementar_pontos(self, partida: Partida):
        primeira_equipe = self.__controlador_sistema.controlador_equipe.busca_equipe_por_nome(partida.primeira_equipe)
        segunda_equipe = self.__controlador_sistema.controlador_equipe.busca_equipe_por_nome(partida.segunda_equipe)
        if partida.gols_primeira_equipe > partida.gols_segunda_equipe:
            primeira_equipe.pontos -= 3
        elif partida.gols_primeira_equipe == partida.gols_segunda_equipe:
            primeira_equipe.pontos -= 1
            segunda_equipe.pontos -= 1
        else:
            segunda_equipe.pontos -= 3

    # Registra as partidas automaticamente a partir das equipes e arbitros existentes
    def registar_partidas(self):
        data_inicial = dt.date.today()
        data_da_partida = data_inicial

        equipes = []
        for equipe in self.__controlador_sistema.controlador_equipe.equipes:
            equipes.append(equipe)

        numero_da_partida = 1
        for i, equipe_um in enumerate(equipes):
            for equipe_dois in equipes[i + 1:]:
                arbitro = random.choice(self.__controlador_sistema.controlador_arbitro.arbitros)
                self.__controlador_sistema.controlador_arbitro.adiciona_partida(arbitro)

                gols_primeira_equipe = random.randint(0, 10)
                gols_segunda_equipe = random.randint(0, 10)
                equipe_um.saldo_de_gols = equipe_um.saldo_de_gols + gols_primeira_equipe
                equipe_dois.saldo_de_gols = equipe_dois.saldo_de_gols + gols_segunda_equipe

                nova_partida = Partida(int(numero_da_partida), data_da_partida, equipe_um.nome, equipe_dois.nome, 
                                       arbitro.nome, gols_primeira_equipe, gols_segunda_equipe)

                self.__partida_dao.add(nova_partida)
                self.acrescentar_pontos(nova_partida)
                self.__controlador_sistema.controlador_campeonato.classificacao()
                numero_da_partida = numero_da_partida + 1
                data_da_partida = data_da_partida + dt.timedelta(days=1)
        
        self.__tela_partida.mostra_mensagem("Partidas cadastradas com sucesso!")

    # Exclui uma partida existente
    def excluir_partida(self):
        if len(self.__partida_dao.get_all()) != 0:
            numero_partida = self.__tela_partida.seleciona_partida()
            partida = self.busca_partida_por_numero(numero_partida)

            if partida is not None:
                self.decrementar_pontos(partida)
                primeira_equipe = self.__controlador_sistema.controlador_equipe.busca_equipe_por_nome(partida.primeira_equipe)
                segunda_equipe = self.__controlador_sistema.controlador_equipe.busca_equipe_por_nome(partida.segunda_equipe)
                primeira_equipe.saldo_de_gols -= partida.gols_primeira_equipe
                segunda_equipe.saldo_de_gols -= partida.gols_segunda_equipe
                self.__partida_dao.remove(partida)
                self.__tela_partida.mostra_mensagem("Partida excluida!")
            else:
                self.__tela_partida.mostra_mensagem("ATENCAO: Esta partida nao existe!")

    # Lista as partidas existentes no campeonato
    def listar_partidas(self):
        if len(self.__partida_dao.get_all()) != 0:
            self.__tela_partida.mostra_mensagem("Partidas cadastradas:")
            for partida in self.__partida_dao.get_all():
                self.__tela_partida.mostra_partida({"numero": partida.numero, "data": partida.data, "primeira_equipe": partida.primeira_equipe, 
                                                    "segunda_equipe": partida.segunda_equipe, "arbitro": partida.arbitro, "gols_primeira_equipe": partida.gols_primeira_equipe, 
                                                    "gols_segunda_equipe": partida.gols_segunda_equipe})
        else:
            self.__tela_partida.mostra_mensagem("ATENCAO: Ainda nao existem partidas!")

    # Finaliza o uso do controlador e volta para o sistema principal
    def finalizar(self):
        self.__controlador_sistema.abre_tela()

    # Abre tela de opcoes
    def abre_tela(self):
        lista_opcoes = {0: self.finalizar, 1: self.registar_partidas, 2: self.excluir_partida, 3: self.listar_partidas}
        while True:
            lista_opcoes[self.__tela_partida.tela_opcoes()]()
