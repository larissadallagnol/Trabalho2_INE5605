# Tela Curso

import PySimpleGUI as sg

class TelaCurso:
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
            [sg.Text('CURSOS', font=("Helvica", 25))],
            [sg.Text('Escolha sua opção', font=("Helvica", 15))],
            [sg.Radio('Cadastrar', "RD1", key='1')],
            [sg.Radio('Editar', "RD1", key='2')],
            [sg.Radio('Excluir', "RD1", key='3')],
            [sg.Radio('Listar', "RD1", key='4')],
            [sg.Radio('Voltar', "RD1", key='0')],
            [sg.Button('Confirmar'), sg.Cancel('Cancelar')]
        ]
        self.__window = sg.Window('Cursos').Layout(layout)

    def pega_dados_curso(self):
        sg.ChangeLookAndFeel('DarkTeal4')
        layout = [
            [sg.Text('DADOS CURSOS', font=("Helvica", 25))],
            [sg.Text('Codigo:', size=(15, 1)), sg.InputText('', key='codigo')],
            [sg.Text('Nome:', size=(15, 1)), sg.InputText('', key='nome')],
            [sg.Button('Confirmar'), sg.Cancel('Cancelar')]
        ]
        self.__window = sg.Window('Dados do Curso').Layout(layout)

        button, values = self.__window.Read()
        codigo = values['codigo']
        nome = values['nome']
        equipes = []
        self.close()
        return {"codigo": codigo, "nome": nome, "equipes": equipes}

    def mostra_curso(self, dados_curso):
        string_curso = (f"CODIGO DO CURSO: {dados_curso['codigo']}\n"
                        f"NOME DO CURSO: {dados_curso['nome']}\n\n")
        sg.Popup('CURSO', string_curso)

    def seleciona_curso(self):
        sg.ChangeLookAndFeel('DarkTeal4')
        layout = [
            [sg.Text('SELECIONAR CURSO', font=("Helvica", 25))],
            [sg.Text('Digite o código do curso que deseja selecionar:', font=("Helvica", 15))],
            [sg.Text('Codigo:', size=(15, 1)), sg.InputText('', key='codigo')],
            [sg.Button('Confirmar'), sg.Cancel('Cancelar')]
        ]
        self.__window = sg.Window('Seleciona Curso').Layout(layout)

        button, values = self.__window.Read()
        codigo = values['codigo']
        self.close()
        return codigo

    def mostra_mensagem(self, msg):
        sg.popup("", msg)

    def close(self):
        self.__window.Close()
