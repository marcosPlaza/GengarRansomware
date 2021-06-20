## ***Gengar Ransomware***

![Gengar Sprite](./gengar-sprite.png)

Interpretación propia del *malware*. Por el momento cuenta con las siguientes caracteríasticas:

* Evasión de entornos virtualizados mediante el módulo *VirtualEnvironmentDetector*
* Programa para encriptar y desencriptar
* Bypass de la *UAC* para elevar privilegios en ejecutar *Encryption_Protocol.py*
* Generación de la *ransom note*
* Macro dropper para descargar y ejecutar el *payload* desde el servidor
* Servidor utilizando túnnel *ngrok*
* Soporte para la visualización del estado de los ataques

## ¡ADVERTENCIA, NO EJECUTAR EL SCRIPT ENCRYPTION_PROTOCOL.PY O .EXE. CIFRA TODOS LOS ARCHIVOS DEL SISTEMA!

### Rutina de cifrado

Para obtener el *payload* como ejecutable, estar en el directorio ``GengarProject`` y ejecutar ``pyinstaller`` . Debemos asegurar que los parámetros que le pasamos a la función execute estan a ``True`` si se quiere; realizar el control anti máquinas virtuales (``antivm=True``), enviar peticion al servidor (``send_post=True``) o si se desea utilizar en su versión ejecutable (``executable=True``).

````powershell
pyinstaller --onefile --windowed Encryption_Protocol.py
````

Si se desea ejecutar el script, poner ``executable=False`` dentro de ``execute()`` en ``Encryption_Protocol.py``.

````
python Encryption_Protocol.py
````

Para iniciar el servidor, ejecutar ``python GengarServer.py``. Atención, se deben modificar las url de ``Encryption_Protocol.py`` y ``Decryptioin_Protocol.py``, por la nueva generada en ejecutar el server.
