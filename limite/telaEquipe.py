# Tela Equipe

class TelaEquipe():
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
        print("--------- EQUIPES ---------")
        print("1 - Cadastrar")
        print("2 - Editar")
        print("3 - Excluir")
        print("4 - Listar")
        print("0 - Voltar")
        opcao = int(self.le_num_inteiro("Escolha a opcao: ", [1, 2, 3, 4, 0]))
        return opcao
    
    def pega_dados_equipe(self):
        print("--------- DADOS EQUIPES ---------")
        nome = input("Nome: ")
        curso = int(input("Codigo do Curso: "))
        lista_alunos = input("CPF's dos alunos: ")
        pontos = 0
        saldo_de_gols = 0

        return {"nome": nome, "curso": curso, "lista_alunos": lista_alunos, "pontos": pontos, "saldo_de_gols": saldo_de_gols}

    def mostra_equipe(self, dados_equipe):
        print("NOME DA EQUIPE: ", dados_equipe["nome"])
        print("CURSO DA EQUIPE: ", dados_equipe["curso"])
        print("LISTA DE ALUNOS DA EQUIPE: ", dados_equipe["lista_alunos"])
        print("PONTOS DA EQUIPE: ", dados_equipe["pontos"])
        print("SALDO DE GOLS DA EQUIPE:", dados_equipe["saldo_de_gols"])
        print("\n")

    def seleciona_equipe(self):
        nome = input("Nome da equipe que deseja selecionar: ")
        return nome

    def mostra_mensagem(self, msg):
        print(msg)
