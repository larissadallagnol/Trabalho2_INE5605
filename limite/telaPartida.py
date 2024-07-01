# Tela Partida

import PySimpleGUI as sg

class TelaPartida:
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
        elif values['0'] or button in (None, 'Cancelar'):
            opcao = 0
        self.close()
        return opcao

    def init_opcoes(self):
        sg.ChangeLookAndFeel('DarkTeal4')
        layout = [
            [sg.Text('PARTIDAS', font=("Helvica", 25))],
            [sg.Text('Escolha sua opção', font=("Helvica", 15))],
            [sg.Radio('Registrar', "RD1", key='1')],
            [sg.Radio('Excluir', "RD1", key='2')],
            [sg.Radio('Listar', "RD1", key='3')],
            [sg.Radio('Voltar', "RD1", key='0')],
            [sg.Button('Confirmar'), sg.Cancel('Cancelar')]
        ]
        self.__window = sg.Window('Partidas').Layout(layout)

    def pega_dados_partida(self):
        sg.ChangeLookAndFeel('DarkTeal4')
        layout = [
            [sg.Text('DADOS PARTIDA', font=("Helvica", 25))],
            [sg.Text('Número:', size=(15, 1)), sg.InputText('', key='numero')],
            [sg.Text('Data:', size=(15, 1)), sg.InputText('', key='data')],
            [sg.Text('Equipe 1:', size=(15, 1)), sg.InputText('', key='primeira_equipe')],
            [sg.Text('Equipe 2:', size=(15, 1)), sg.InputText('', key='segunda_equipe')],
            [sg.Text('Árbitro:', size=(15, 1)), sg.InputText('', key='arbitro')],
            [sg.Text('Gols Equipe 1:', size=(15, 1)), sg.InputText('', key='gols_primeira_equipe')],
            [sg.Text('Gols Equipe 2:', size=(15, 1)), sg.InputText('', key='gols_segunda_equipe')],
            [sg.Button('Confirmar'), sg.Cancel('Cancelar')]
        ]
        self.__window = sg.Window('Dados da Partida').Layout(layout)

        button, values = self.__window.Read()
        numero = values['numero']
        data = values['data']
        primeira_equipe = values['primeira_equipe']
        segunda_equipe = values['segunda_equipe']
        arbitro = values['arbitro']
        gols_primeira_equipe = values['gols_primeira_equipe']
        gols_segunda_equipe = values['gols_segunda_equipe']
        self.close()
        return {
            "numero": numero,
            "data": data,
            "primeira_equipe": primeira_equipe,
            "segunda_equipe": segunda_equipe,
            "arbitro": arbitro,
            "gols_primeira_equipe": gols_primeira_equipe,
            "gols_segunda_equipe": gols_segunda_equipe,
        }

    def mostra_partida(self, dados_partida):
        string_partida = (f"NÚMERO DA PARTIDA: {dados_partida['numero']}\n"
                          f"DATA DA PARTIDA: {dados_partida['data']}\n"
                          f"EQUIPE 1: {dados_partida['primeira_equipe']}\n"
                          f"EQUIPE 2: {dados_partida['segunda_equipe']}\n"
                          f"ÁRBITRO: {dados_partida['arbitro']}\n"
                          f"GOLS EQUIPE 1: {dados_partida['gols_primeira_equipe']}\n"
                          f"GOLS EQUIPE 2: {dados_partida['gols_segunda_equipe']}\n")
        sg.Popup('PARTIDA', string_partida)

    def seleciona_partida(self):
        sg.ChangeLookAndFeel('DarkTeal4')
        layout = [
            [sg.Text('SELECIONAR PARTIDA', font=("Helvica", 25))],
            [sg.Text('Digite o número da partida que deseja selecionar:', font=("Helvica", 15))],
            [sg.Text('Número:', size=(15, 1)), sg.InputText('', key='numero')],
            [sg.Button('Confirmar'), sg.Cancel('Cancelar')]
        ]
        self.__window = sg.Window('Seleciona Partida').Layout(layout)

        button, values = self.__window.Read()
        numero = values['numero']
        self.close()
        return numero

    def mostra_mensagem(self, msg):
        sg.popup("", msg)

    def close(self):
        self.__window.Close()
