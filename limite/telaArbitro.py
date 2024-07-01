# Tela Arbitro

class TelaArbitro():
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
        print("--------- ARBITROS ---------")
        print("1 - Cadastrar")
        print("2 - Editar")
        print("3 - Excluir")
        print("4 - Listar")
        print("0 - Voltar")
        opcao = int(self.le_num_inteiro("Escolha a opcao: ", [1, 2, 3, 4, 0]))
        return opcao
    
    def pega_dados_arbitro(self):
        print("--------- DADOS ARBITROS ---------")
        nome = input("Nome: ")
        cpf = input("CPF: ")
        data_de_nascimento = input("Data-de-Nascimento: ")
        numero_partidas = 0

        return {"nome": nome, "cpf": cpf, "data_de_nascimento": data_de_nascimento, "numero_partidas": numero_partidas}

    def mostra_arbitro(self, dados_arbitro):
        print("NOME DO ARBITRO: ", dados_arbitro["nome"])
        print("CPF DO ARBITRO: ", dados_arbitro["cpf"])
        print("DATA DE NASCIMENTO DO ARBITRO: ", dados_arbitro["data_de_nascimento"])
        print("NUMERO DE PARTIDAS DO ARBITRO: ", dados_arbitro["numero_partidas"])
        print("\n")

    def seleciona_arbitro(self):
        cpf = input("CPF do arbitro que deseja selecionar: ")
        return cpf

    def mostra_mensagem(self, msg):
        print(msg)
