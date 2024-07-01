# Tela geral do sistema

import PySimpleGUI as sg

class TelaSistema:
    def __init__(self):
        self.__window = None
        self.init_components()

    def tela_opcoes(self):
        self.init_components()
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
        elif values['5']:
            opcao = 5
        elif values['6']:
            opcao = 6
        elif values['7']:
            opcao = 7
        elif values['0'] or button in (None, 'Cancelar'):
            opcao = 0
        self.close()
        return opcao

    def close(self):
        self.__window.Close()

    def init_components(self):
        sg.ChangeLookAndFeel('DarkTeal4')
        layout = [
            [sg.Text('SISTEMA CAMPEONATOS', font=("Helvica", 25))],
            [sg.Text('Escolha sua opção', font=("Helvica", 15))],
            [sg.Radio('Cursos', "RD1", key='1')],
            [sg.Radio('Alunos', "RD1", key='2')],
            [sg.Radio('Arbitros', "RD1", key='3')],
            [sg.Radio('Equipes', "RD1", key='4')],
            [sg.Radio('Partidas', "RD1", key='5')],
            [sg.Radio('Campeonatos', "RD1", key='6')],
            [sg.Radio('Relatorios', 'RD1', key='7')],
            [sg.Radio('Finalizar sistema', "RD1", key='0')],
            [sg.Button('Confirmar'), sg.Cancel('Cancelar')]
        ]
        self.__window = sg.Window('Sistema de Campeonatos').Layout(layout)
