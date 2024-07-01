# Tela Campeonato

import PySimpleGUI as sg

class TelaCampeonato:
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
            [sg.Text('CAMPEONATOS', font=("Helvica", 25))],
            [sg.Text('Escolha sua opção', font=("Helvica", 15))],
            [sg.Radio('Cadastrar', "RD1", key='1')],
            [sg.Radio('Editar', "RD1", key='2')],
            [sg.Radio('Excluir', "RD1", key='3')],
            [sg.Radio('Listar', "RD1", key='4')],
            [sg.Radio('Voltar', "RD1", key='0')],
            [sg.Button('Confirmar'), sg.Cancel('Cancelar')]
        ]
        self.__window = sg.Window('Sistema de Campeonatos').Layout(layout)

    def pega_dados_campeonato(self):
        sg.ChangeLookAndFeel('DarkTeal4')
        layout = [
            [sg.Text('DADOS CAMPEONATO', font=("Helvica", 25))],
            [sg.Text('Nome:', size=(15, 1)), sg.InputText('', key='nome')],
            [sg.Text('Equipes:', size=(15, 1)), sg.InputText('', key='lista_equipes')],
            [sg.Text('Código das partidas:', size=(15, 1)), sg.InputText('', key='lista_partidas')],
            [sg.Button('Confirmar'), sg.Cancel('Cancelar')]
        ]
        self.__window = sg.Window('Dados do Campeonato').Layout(layout)

        button, values = self.__window.Read()
        nome = values['nome']
        lista_equipes = values['lista_equipes']
        lista_partidas = values['lista_partidas']
        self.close()
        return {"nome": nome, "lista_equipes": lista_equipes, "lista_partidas": lista_partidas}

    def mostra_campeonato(self, dados_campeonato):
        string_campeonato = (f"NOME DO CAMPEONATO: {dados_campeonato['nome']}\n"
                             f"EQUIPES DO CAMPEONATO: {dados_campeonato['lista_equipes']}\n"
                             f"PARTIDAS DO CAMPEONATO: {dados_campeonato['lista_partidas']}\n\n")
        sg.Popup('CAMPEONATO', string_campeonato)

    def seleciona_campeonato(self):
        sg.ChangeLookAndFeel('DarkTeal4')
        layout = [
            [sg.Text('SELECIONAR CAMPEONATO', font=("Helvica", 25))],
            [sg.Text('Digite o nome do campeonato que deseja selecionar:', font=("Helvica", 15))],
            [sg.Text('Nome:', size=(15, 1)), sg.InputText('', key='nome')],
            [sg.Button('Confirmar'), sg.Cancel('Cancelar')]
        ]
        self.__window = sg.Window('Seleciona Campeonato').Layout(layout)

        button, values = self.__window.Read()
        nome = values['nome']
        self.close()
        return nome

    def mostra_mensagem(self, msg):
        sg.popup("", msg)

    def close(self):
        self.__window.Close()
