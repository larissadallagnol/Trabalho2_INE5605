# Tela Partida

class TelaPartida():
    # Tratamento da entrada de dados
    def le_num_inteiro(self, mensagem: str = "", inteiros_validos: list = None):
        while True:
            valor_lido = input(mensagem)
            try:
                inteiro = int(valor_lido)
                if inteiros_validos and inteiro not in inteiros_validos:
                    raise ValueError
                return inteiro
            except ValueError:
                print("Valor incorreto: Digite um valor numerico inteiro valido")
                if inteiros_validos:
                    print("Valores validos: ", inteiros_validos)

    def mostra_tela_opcoes(self):
        print("--------- PARTIDAS ---------")
        print("1 - Registrar")
        print("2 - Excluir")
        print("3 - Listar")
        print("0 - Voltar")
        opcao = int(self.le_num_inteiro("Escolha a opcao: ", [1, 2, 3, 0]))
        return opcao

    def mostra_partida(self, dados_partida):
        print("NUMERO DA PARTIDA: ", dados_partida["numero"])
        print("DATA DA PARTIDA: ", dados_partida["data"])
        print("EQUIPE 1 DA PARTIDA: ", dados_partida["primeira_equipe"])
        print("EQUIPE 2 DA PARTIDA: ", dados_partida["segunda_equipe"])
        print("ARBITRO DA PARTIDA: ", dados_partida["arbitro"])
        print("GOLS DA EQUIPE 1: ", dados_partida["gols_primeira_equipe"])
        print("GOLS DA EQUIPE 2: ", dados_partida["gols_segunda_equipe"])
        print("\n")

    def seleciona_partida(self):
        numero = int(input("Numero da partida que deseja selecionar: "))
        return numero

    def mostra_mensagem(self, msg):
        print(msg)
