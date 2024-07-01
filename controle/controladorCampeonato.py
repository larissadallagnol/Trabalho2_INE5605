# Controlador Campeonato

from entidade.campeonato import Campeonato
from limite.telaCampeonato import TelaCampeonato
from persistencia.campeonatoDAO import CampeonatoDAO

class ControladorCampeonato():
    def __init__(self, controlador_sistema):
        self.__tela_campeonato = TelaCampeonato()
        self.__campeonato_dao = CampeonatoDAO()
        self.__controlador_sistema = controlador_sistema
    
    @property
    def campeonatos(self):
        return self.__campeonato_dao.get_all()

    # Busca um cameponato pelo nome dele
    def busca_campeonato_por_nome(self, nome: str):
        for campeonato in self.__campeonato_dao.get_all():
            if campeonato.nome == nome:
                return campeonato
        return None
    
    # Define a classificacao do campeonato    
    def classificacao(self):
        # Cria uma lista de tuplas (nome da equipe, pontos, saldo de gols)
        equipes_pontos = [(equipe.nome, equipe.pontos, equipe.saldo_de_gols) for equipe in self.__controlador_sistema.controlador_equipe.equipes]

        # Ordena a lista de tuplas em ordem decrescente de pontos e, em caso de empate, saldo de gols
        equipes_pontos.sort(key=lambda x: (x[1], x[2]), reverse=True)

        # Cria o dicionário de classificacao
        classificacao = {str(index + 1): equipe[0] for index, equipe in enumerate(equipes_pontos)}

        return classificacao

    # Cadastra um novo campeonato
    def cadastrar_campeonato(self):
        dados_campeonato = self.__tela_campeonato.pega_dados_campeonato()
        existe_campeonato = False
        for campeonato in self.__campeonato_dao.get_all():
            if campeonato.nome == dados_campeonato["nome"]:
                existe_campeonato = True
        if existe_campeonato is False:
            lista_equipes = []
            nome_split = dados_campeonato["lista_equipes"].split(',')
            for nome in nome_split:
                equipe = self.__controlador_sistema.controlador_equipe.busca_equipe_por_nome(nome)
                lista_equipes.append(equipe.nome)
            lista_partidas = []
            numero_split = dados_campeonato["lista_partidas"].split()
            for numero in numero_split:
                partida = self.__controlador_sistema.controlador_partida.busca_partida_por_numero(int(numero))
                lista_partidas.append("Partida {}: {} versus {}.".format(partida.numero, partida.primeira_equipe, partida.segunda_equipe))
            novo_campeonato = Campeonato(dados_campeonato["nome"], lista_equipes, lista_partidas)
            self.__campeonato_dao.add(novo_campeonato)
            self.__tela_campeonato.mostra_mensagem("Campeonato cadastrado com sucesso!")
        else:
            self.__tela_campeonato.mostra_mensagem("ATENCAO: Campeonato ja existente!")

    # Edita um campeonato existente
    def editar_campeonato(self):
        if len(self.__campeonato_dao.get_all()) != 0:
            nome_campeonato = self.__tela_campeonato.seleciona_campeonato()
            campeonato = self.busca_campeonato_por_nome(nome_campeonato)

            if campeonato is not None:
                novos_dados_campeonato = self.__tela_campeonato.pega_dados_campeonato()
                campeonato.nome = novos_dados_campeonato["nome"]
                lista_equipes = []
                nome_split = novos_dados_campeonato["lista_equipes"].split()
                for nome in nome_split:
                    lista_equipes.append(self.__controlador_sistema.controlador_equipe.busca_equipe_por_nome(nome))
                campeonato.equipes = lista_equipes
                lista_partidas = []
                numero_split = novos_dados_campeonato["lista_partidas"].split()
                for numero in numero_split:
                    lista_partidas.append(self.__controlador_sistema.controlador_partida.busca_partida_por_numero(numero))
                campeonato.partidas = lista_partidas
                self.__campeonato_dao.update(campeonato)
                self.__tela_campeonato.mostra_mensagem("Campeonato editado com sucesso!")
            else:
                self.__tela_campeonato.mostra_mensagem("ATENCAO: Este campeonato nao existe!")

    # Exclui um campeonato existente
    def excluir_campeonato(self):
        if len(self.__campeonato_dao.get_all()) != 0:
            nome_campeonato = self.__tela_campeonato.seleciona_campeonato()
            campeonato = self.busca_campeonato_por_nome(nome_campeonato)

            if campeonato is not None:
                self.__campeonato_dao.remove(campeonato)
                self.__tela_campeonato.mostra_mensagem("Campeonato excluido!")
            else:
                self.__tela_campeonato.mostra_mensagem("ATENCAO: Este campeonato nao existe!")

    # Lista os campeonatos existentes
    def listar_campeonatos(self):
        if len(self.__campeonato_dao.get_all()) != 0:
            self.__tela_campeonato.mostra_mensagem("Campeonatos cadastrados:")
            for campeonato in self.__campeonato_dao.get_all():
                self.__tela_campeonato.mostra_campeonato({"nome": campeonato.nome, "lista_equipes": campeonato.equipes, "lista_partidas": campeonato.partidas})
                self.classificacao()
        else:
            self.__tela_campeonato.mostra_mensagem("ATENCAO: Ainda nao existem campeonatos!")

    # Finaliza o uso do controlador e volta para o sistema principal
    def finalizar(self):
        self.__controlador_sistema.abre_tela()

    # Abre tela de opcoes
    def abre_tela(self):
        lista_opcoes = {0: self.finalizar, 1: self.cadastrar_campeonato, 2: self.editar_campeonato, 3: self.excluir_campeonato, 4: self.listar_campeonatos}
        while True:
            lista_opcoes[self.__tela_campeonato.tela_opcoes()]()
