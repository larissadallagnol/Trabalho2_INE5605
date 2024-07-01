# Tela Equipe

import PySimpleGUI as sg

class TelaEquipe:
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
            [sg.Text('EQUIPES', font=("Helvica", 25))],
            [sg.Text('Escolha sua opção', font=("Helvica", 15))],
            [sg.Radio('Cadastrar', "RD1", key='1')],
            [sg.Radio('Editar', "RD1", key='2')],
            [sg.Radio('Excluir', "RD1", key='3')],
            [sg.Radio('Listar', "RD1", key='4')],
            [sg.Radio('Voltar', "RD1", key='0')],
            [sg.Button('Confirmar'), sg.Cancel('Cancelar')]
        ]
        self.__window = sg.Window('Equipes').Layout(layout)

    def pega_dados_equipe(self):
        sg.ChangeLookAndFeel('DarkTeal4')
        layout = [
            [sg.Text('DADOS EQUIPES', font=("Helvica", 25))],
            [sg.Text('Nome:', size=(15, 1)), sg.InputText('', key='nome')],
            [sg.Text('Código do Curso:', size=(15, 1)), sg.InputText('', key='curso')],
            [sg.Text('CPF\'s dos alunos:', size=(15, 1)), sg.InputText('', key='lista_alunos')],
            [sg.Button('Confirmar'), sg.Cancel('Cancelar')]
        ]
        self.__window = sg.Window('Dados da Equipe').Layout(layout)

        button, values = self.__window.Read()
        nome = values['nome']
        curso = values['curso']
        lista_alunos = values['lista_alunos']
        pontos = 0
        saldo_de_gols = 0
        self.close()
        return {"nome": nome, "curso": curso, "lista_alunos": lista_alunos, "pontos": pontos, "saldo_de_gols": saldo_de_gols}

    def mostra_equipe(self, dados_equipe):
        string_equipe = (f"NOME DA EQUIPE: {dados_equipe['nome']}\n"
                         f"CURSO DA EQUIPE: {dados_equipe['curso']}\n"
                         f"LISTA DE ALUNOS DA EQUIPE: {dados_equipe['lista_alunos']}\n\n")
        sg.Popup('EQUIPE', string_equipe)

    def seleciona_equipe(self):
        sg.ChangeLookAndFeel('DarkTeal4')
        layout = [
            [sg.Text('SELECIONAR EQUIPE', font=("Helvica", 25))],
            [sg.Text('Digite o nome da equipe que deseja selecionar:', font=("Helvica", 15))],
            [sg.Text('Nome:', size=(15, 1)), sg.InputText('', key='nome')],
            [sg.Button('Confirmar'), sg.Cancel('Cancelar')]
        ]
        self.__window = sg.Window('Seleciona Equipe').Layout(layout)

        button, values = self.__window.Read()
        nome = values['nome']
        self.close()
        return nome

    def mostra_mensagem(self, msg):
        sg.popup("", msg)

    def close(self):
        self.__window.Close()
