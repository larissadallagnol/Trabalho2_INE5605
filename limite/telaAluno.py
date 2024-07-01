# Tela Aluno 

class TelaAluno():
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
        print("--------- ALUNOS ---------")
        print("1 - Cadastrar")
        print("2 - Editar")
        print("3 - Excluir")
        print("4 - Listar")
        print("0 - Voltar")
        opcao = int(self.le_num_inteiro("Escolha a opcao: ", [1, 2, 3, 4, 0]))
        return opcao
    
    def pega_dados_aluno(self):
        print("--------- DADOS ALUNO ---------")
        nome = input("Nome: ")
        cpf = input("CPF: ")
        data_de_nascimento = input("Data-de-Nascimento: ")
        matricula = input("Matricula: ")
        curso = int(input("Codigo-do-Curso: "))

        return {"nome": nome, "cpf": cpf, "data_de_nascimento": data_de_nascimento, "matricula": matricula, "curso": curso}

    def mostra_aluno(self, dados_aluno):
        print("NOME DO ALUNO: ", dados_aluno["nome"])
        print("CPF DO ALUNO: ", dados_aluno["cpf"])
        print("DATA DE NASCIMENTO DO ALUNO: ", dados_aluno["data_de_nascimento"])
        print("MATRICULA DO ALUNO: ", dados_aluno["matricula"])
        print("CURSO DO ALUNO: ", dados_aluno["curso"])
        print("\n")

    def seleciona_aluno(self):
        cpf = input("CPF do aluno que deseja selecionar: ")
        return cpf

    def mostra_mensagem(self, msg):
        print(msg)
