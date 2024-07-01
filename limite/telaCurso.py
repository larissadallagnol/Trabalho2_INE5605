# Tela Curso

class TelaCurso():
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
        print("--------- CURSOS ---------")
        print("1 - Cadastrar")
        print("2 - Editar")
        print("3 - Excluir")
        print("4 - Listar")
        print("0 - Voltar")
        opcao = int(self.le_num_inteiro("Escolha a opcao: ", [1, 2, 3, 4, 0]))
        return opcao
    
    def pega_dados_curso(self):
        print("--------- DADOS CURSOS ---------")
        codigo = int(input("Codigo: "))
        nome = input("Nome: ")
        equipes = []

        return {"codigo": codigo, "nome": nome, "equipes": equipes}

    def mostra_curso(self, dados_curso):
        print("CODIGO DO CURSO: ", dados_curso["codigo"])
        print("NOME DO CURSO: ", dados_curso["nome"])
        print("EQUIPES DO CURSO: ", dados_curso["equipes"])
        print("\n")

    def seleciona_curso(self):
        codigo = int(input("Codigo do curso que deseja selecionar: "))
        return codigo

    def mostra_mensagem(self, msg):
        print(msg)
