from PySimpleGUI import PySimpleGUI as sg
import os

sg.theme('Reddit')

layout = [[sg.Text("IP:")],
          [sg.Input(key='ip')],
          [sg.Text("Mascara:")],
          [sg.Input(key='mask')],
          [sg.Text("Gateway:")],
          [sg.Input(key='gateway')],
          [sg.Button('Inserir', key='Add'), sg.Button('Deletar', key='Delete'), sg.Button('Sair', key='Quit')]]

window = sg.Window('Criação de rotas - Fagner Mendes', layout)

csv_rows = []

while True:

    evento, values = window.read()

    if evento == 'Add':
        
        ip_adress = values['ip']
        net_mask = values['mask']
        gateway = values['gateway']

        os.system(f"route add {ip_adress} mask {net_mask} {gateway} metric 1")
        
    elif evento == 'Delete':
      
        ip_adress = values['ip']
        net_mask = values['mask']
        gateway = values['gateway']

        os.system(f"route delete {ip_adress} mask {net_mask} {gateway}")

    else:
        
        break

window.close()
