from cryptography.fernet import Fernet
import subprocess
import Utils

class Cipher(Utils.Utils):
    def __init__(self):
        self.key = Fernet.generate_key()
        self.fernet = Fernet(self.key)

    def save_key_as_file(self, hidden=True):
        with open('key.key', 'wb') as key_file:
            key_file.write(self.key)

        if hidden:
            try:
                subprocess.check_call(['attrib', '+h', 'key.key'])
            except:
                pass

    def load_key_from_file(self):
        return open("key.key", "rb").read()

    def symmetric_encrypt_or_decrypt(self, full_path, key, opt='encrypt'):
        try:
            data = self.load_data(full_path)
            if opt == 'encrypt':
                encrypted_data = self.fernet.encrypt(data)
                self.save_data(full_path, encrypted_data)
            elif opt == 'decrypt':
                decrypted_data = self.fernet.decrypt(data)
                self.save_data(full_path, decrypted_data, 'del_ext')
            else:
                raise ValueError('Invalid argument')
        except ValueError as ve:
            print(ve)
        except PermissionError as pe:
            print(pe)
        except IOError as ioe:
            print(ioe)
