# Controlador Arbitro

from entidade.arbitro import Arbitro
from limite.telaArbitro import TelaArbitro

class ControladorArbitro():
    def __init__(self, controlador_sistema):
        self.__tela_arbitro = TelaArbitro()
        self.__arbitros = []
        self.__controlador_sistema = controlador_sistema
    
    @property
    def arbitros(self):
        return self.__arbitros
    
    # Adiciona uma partida ao numero de partidas de um arbitro
    def adiciona_partida(self, arbitro: Arbitro):
        for _arbitro in self.__arbitros:
            if _arbitro is arbitro:
                arbitro.numero_partidas = int(arbitro.numero_partidas) + 1

    # Busca um arbitro pelo CPF dele
    def busca_arbitro_por_cpf(self, cpf: int):
        for arbitro in self.__arbitros:
            if arbitro.cpf == cpf:
                return arbitro
        return None

    # Cadastra um novo arbitro
    def cadastrar_arbitro(self):
        dados_arbitro = self.__tela_arbitro.pega_dados_arbitro()
        existe_arbitro = False
        for arbitro in self.__arbitros:
            if arbitro.cpf == dados_arbitro["cpf"]:
                existe_arbitro = True
        if existe_arbitro is False:
            novo_arbitro = Arbitro(dados_arbitro["nome"], dados_arbitro["cpf"], 
                                   dados_arbitro["data_de_nascimento"], dados_arbitro["numero_partidas"])
            self.__arbitros.append(novo_arbitro)
            self.__tela_arbitro.mostra_mensagem("Arbitro cadastrado com sucesso!")
        else:
            self.__tela_arbitro.mostra_mensagem("ATENCAO: Arbitro ja existente!")

    # Edita um arbitro existente
    def editar_arbitro(self):
        self.listar_arbitros()
        cpf_arbitro = self.__tela_arbitro.seleciona_arbitro()
        arbitro = self.busca_arbitro_por_cpf(cpf_arbitro)

        if arbitro is not None:
            novos_dados_arbitro = self.__tela_arbitro.pega_dados_arbitro()
            arbitro.nome = novos_dados_arbitro["nome"]
            arbitro.cpf = novos_dados_arbitro["cpf"]
            arbitro.data_de_nascimento = novos_dados_arbitro["data_de_nascimento"]
            arbitro.numero_partidas = novos_dados_arbitro["numero_partidas"]
            self.__tela_arbitro.mostra_mensagem("Arbitro editado com sucesso!")
        else:
            self.__tela_arbitro.mostra_mensagem("ATENCAO: Este arbitro nao existe!")

    # Exclui um arbitro existente
    def excluir_arbitro(self):
        self.listar_arbitros()
        cpf_arbitro = self.__tela_arbitro.seleciona_arbitro()
        arbitro = self.busca_arbitro_por_cpf(cpf_arbitro)

        if arbitro is not None:
            self.__arbitros.remove(arbitro)
            self.__tela_arbitro.mostra_mensagem("Arbitro excluido com sucesso!")
        else:
            self.__tela_arbitro.mostra_mensagem("ATENCAO: Este arbitro nao existe!")

    # Lista os arbitros existentes
    def listar_arbitros(self):
        if len(self.__arbitros) != 0:
            self.__tela_arbitro.mostra_mensagem("Arbitros cadastrados:")
            for arbitro in self.__arbitros:
                self.__tela_arbitro.mostra_arbitro({"nome": arbitro.nome, "cpf": arbitro.cpf, 
                                                    "data_de_nascimento": arbitro.data_de_nascimento, 
                                                    "numero_partidas": arbitro.numero_partidas})
        else:
            self.__tela_arbitro.mostra_mensagem("ATENCAO: Ainda nao existem arbitros!")

    # Finaliza o uso do controlador e volta para o sistema principal
    def finalizar(self):
        self.__controlador_sistema.abre_tela()

    # Abre tela de opcoes
    def abre_tela(self):
        lista_opcoes = {0: self.finalizar, 1: self.cadastrar_arbitro, 2: self.editar_arbitro, 
                        3: self.excluir_arbitro, 4: self.listar_arbitros}
        while True:
            lista_opcoes[self.__tela_arbitro.mostra_tela_opcoes()]()
