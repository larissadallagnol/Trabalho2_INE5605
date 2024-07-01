# Controlador Relatorio

from limite.telaRelatorio import TelaRelatorio

class ControladorRelatorio():
    def __init__(self, controlador_sistema):
        self.__tela_relatorio = TelaRelatorio()
        self.__controlador_sistema = controlador_sistema

    def gerar_relatorio_ganhadores(self):
        classificacao = self.__controlador_sistema.controlador_campeonato.classificacao()
        relatorio = "Classificação do Campeonato:\n"
        
        for posicao in ["1", "2", "3"]:
            if posicao in classificacao:
                relatorio += f"{posicao}º Lugar: {classificacao[posicao]}\n"

        self.__tela_relatorio.mostra_relatorio(relatorio)

    def gerar_relatorio_de_classificacao(self):
        classificacao = self.__controlador_sistema.controlador_campeonato.classificacao()
        relatorio = "Classificação do Campeonato:\n"
        
        for posicao, equipe in classificacao.items():
            relatorio += f"{posicao}º Lugar: {equipe}\n"

        self.__tela_relatorio.mostra_relatorio(relatorio)

    
    def gerar_relatorio_equipe_fez_mais_gols(self):
        equipes = self.__controlador_sistema.controlador_equipe.equipes
        equipes_ordenadas = sorted(equipes, key=lambda equipe: equipe.saldo_de_gols, reverse=True)
        relatorio = "Equipes com mais gols:\n"
        
        for i in range(min(3, len(equipes_ordenadas))):
            relatorio += f"{i + 1}º Lugar: {equipes_ordenadas[i].nome} - Gols: {equipes_ordenadas[i].saldo_de_gols}\n"
        
        self.__tela_relatorio.mostra_relatorio(relatorio)


    def finalizar(self):
        self.__controlador_sistema.abre_tela()

    def abre_tela(self):
        lista_opcoes = {
            0: self.finalizar,
            1: self.gerar_relatorio_ganhadores,
            2: self.gerar_relatorio_de_classificacao,
            3: self.gerar_relatorio_equipe_fez_mais_gols
        }
        while True:
            opcao = self.__tela_relatorio.tela_opcoes()
            funcao = lista_opcoes.get(opcao)
            if funcao:
                funcao()

