# Tela Campeonato

class TelaCampeonato():
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
        print("--------- CAMPEONATOS ---------")
        print("1 - Cadastrar")
        print("2 - Editar")
        print("3 - Excluir")
        print("4 - Listar")
        print("0 - Voltar")
        opcao = int(self.le_num_inteiro("Escolha a opcao: ", [1, 2, 3, 4, 0]))
        return opcao
    
    def pega_dados_campeonato(self):
        print("--------- DADOS CAMPEONATO ---------")
        nome = input("Nome: ")
        lista_equipes = input("Nomes das Equipes (separados por virgula): ")
        lista_partidas = input("Codigo das partidas: ")

        return {"nome": nome, "lista_equipes": lista_equipes, "lista_partidas": lista_partidas}

    def mostra_campeonato(self, dados_equipe):
        print("NOME DO CAMPEONATO: ", dados_equipe["nome"])
        print("EQUIPES DO CAMPEONATO: ", dados_equipe["lista_equipes"])
        print("PARTIDAS DO CAMPEONATO: ", dados_equipe["lista_partidas"])
        print("\n")

    def seleciona_campeonato(self):
        nome = input("Nome do campeonato que deseja selecionar: ")
        return nome

    def mostra_mensagem(self, msg):
        print(msg)
