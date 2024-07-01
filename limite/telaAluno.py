# Tela Aluno

import PySimpleGUI as sg

class TelaAluno:
    def __init__(self):
        self.__window = None
        self.init_opcoes()

    def tela_opcoes(self):
        self.init_opcoes()
        button, values = self.__window.Read()
        opcao = 0
        if values['1']:
            opcao = 1
        elif values['2']:
            opcao = 2
        elif values['3']:
            opcao = 3
        elif values['4']:
            opcao = 4
        elif values['0'] or button in (None, 'Cancelar'):
            opcao = 0
        self.close()
        return opcao

    def init_opcoes(self):
        sg.ChangeLookAndFeel('DarkTeal4')
        layout = [
            [sg.Text('ALUNOS', font=("Helvica", 25))],
            [sg.Text('Escolha sua opção', font=("Helvica", 15))],
            [sg.Radio('Cadastrar', "RD1", key='1')],
            [sg.Radio('Editar', "RD1", key='2')],
            [sg.Radio('Excluir', "RD1", key='3')],
            [sg.Radio('Listar', "RD1", key='4')],
            [sg.Radio('Voltar', "RD1", key='0')],
            [sg.Button('Confirmar'), sg.Cancel('Cancelar')]
        ]
        self.__window = sg.Window('Sistema de Alunos').Layout(layout)

    def pega_dados_aluno(self):
        sg.ChangeLookAndFeel('DarkTeal4')
        layout = [
            [sg.Text('DADOS ALUNO', font=("Helvica", 25))],
            [sg.Text('Nome:', size=(15, 1)), sg.InputText('', key='nome')],
            [sg.Text('CPF:', size=(15, 1)), sg.InputText('', key='cpf')],
            [sg.Text('Data de Nascimento:', size=(15, 1)), sg.InputText('', key='data_de_nascimento')],
            [sg.Text('Matricula:', size=(15, 1)), sg.InputText('', key='matricula')],
            [sg.Text('Curso:', size=(15, 1)), sg.InputText('', key='curso')],
            [sg.Button('Confirmar'), sg.Cancel('Cancelar')]
        ]
        self.__window = sg.Window('Dados do Aluno').Layout(layout)

        button, values = self.__window.Read()
        nome = values['nome']
        cpf = values['cpf']
        data_de_nascimento = values['data_de_nascimento']
        matricula = values['matricula']
        curso = values['curso']
        self.close()
        return {"nome": nome, "cpf": cpf, "data_de_nascimento": data_de_nascimento, "matricula": matricula, "curso": curso}

    def mostra_aluno(self, dados_aluno):
        string_aluno = (f"NOME DO ALUNO: {dados_aluno['nome']}\n"
                        f"CPF DO ALUNO: {dados_aluno['cpf']}\n"
                        f"DATA DE NASCIMENTO DO ALUNO: {dados_aluno['data_de_nascimento']}\n"
                        f"MATRICULA DO ALUNO: {dados_aluno['matricula']}\n"
                        f"CURSO DO ALUNO: {dados_aluno['curso']}\n\n")
        sg.Popup('ALUNO', string_aluno)

    def seleciona_aluno(self):
        sg.ChangeLookAndFeel('DarkTeal4')
        layout = [
            [sg.Text('SELECIONAR ALUNO', font=("Helvica", 25))],
            [sg.Text('Digite o CPF do aluno que deseja selecionar:', font=("Helvica", 15))],
            [sg.Text('CPF:', size=(15, 1)), sg.InputText('', key='cpf')],
            [sg.Button('Confirmar'), sg.Cancel('Cancelar')]
        ]
        self.__window = sg.Window('Seleciona Aluno').Layout(layout)

        button, values = self.__window.Read()
        cpf = values['cpf']
        self.close()
        return cpf

    def mostra_mensagem(self, msg):
        sg.popup("", msg)

    def close(self):
        self.__window.Close()
