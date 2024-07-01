# Tela Sistema

class TelaSistema:
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

    def tela_opcoes(self):
        print("--------- SISTEMA CAMPEONATOS ---------")
        print("1 - Cursos")
        print("2 - Alunos")
        print("3 - Arbitros")
        print("4 - Equipes")
        print("5 - Partidas")
        print("6 - Campeonatos")
        print("0 - Finalizar sistema")
        opcao = int(self.le_num_inteiro("Escolha a opcao:", [1, 2, 3, 4, 5, 6, 0]))
        return opcao
