# Tela Relatorio

import PySimpleGUI as sg

class TelaRelatorio:
    def __init__(self):
        self.__window = None

    def tela_opcoes(self):
        sg.theme('DarkTeal4')

        layout = [
            [sg.Text('GERAR RELATÓRIOS', size=(30, 1), font=("Helvetica", 25), justification='center')],
            [sg.Button('Relatório de Ganhadores', size=(30, 2), key='relatorio_ganhadores')],
            [sg.Button('Relatório de Classificação', size=(30, 2), key='relatorio_classificacao')],
            [sg.Button('Relatório de Equipe que Fez Mais Gols', size=(30, 2), key='relatorio_mais_gols')],
            [sg.Button('Voltar', size=(30, 2), key='voltar')],
        ]

        self.__window = sg.Window('Sistema de Campeonato', layout, finalize=True)
        event, _ = self.__window.read()
        self.__window.close()
        if event == 'relatorio_ganhadores':
            return 1
        elif event == 'relatorio_classificacao':
            return 2
        elif event == 'relatorio_mais_gols':
            return 3
        elif event == 'voltar' or event == sg.WINDOW_CLOSED:
            return 0

    def mostra_relatorio(self, relatorio):
        sg.theme('LightGrey1')
        layout = [
            [sg.Text(relatorio, size=(50, 10), font=("Helvetica", 15))],
            [sg.Button('Ok', size=(10, 1))]
        ]
        self.__window = sg.Window('Relatório', layout, finalize=True)
        event, _ = self.__window.read()
        self.__window.close()

    def mostra_mensagem(self, mensagem):
        sg.theme('LightGrey1')
        layout = [
            [sg.Text(mensagem, size=(30, 1), font=("Helvetica", 15))],
            [sg.Button('Ok', size=(10, 1))]
        ]
        self.__window = sg.Window('Mensagem', layout, finalize=True)
        event, _ = self.__window.read()
        self.__window.close()
