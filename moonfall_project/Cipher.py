from cryptography.fernet import Fernet
import subprocess
import Utils


class Cipher(Utils.Utils):
    def __init__(self, key=None, action='decrypt'):
        if key is None:
            self.key = Fernet.generate_key()
        else:
            self.key = key
            
        self.fernet = Fernet(self.key)
        
        if action == 'encrypt':
            msg = str.encode('This is a test file that may be hidden')
            enc_msg = self.fernet.encrypt(msg)
            with open('test.txt', 'wb') as test_file:
                test_file.write(enc_msg)
            try:
                subprocess.check_call(['attrib', '+h', 'test.txt'])
            except:
                print('test.txt cannot be hidden')
        
    def set_key(self, key):
        self.key = key
        
        
    def set_fernet(self, key):
        self.Fernet = Fernet(key)


    def save_key_as_file(self, hidden=True):
        with open('key.key', 'wb') as key_file:
            key_file.write(self.key)

        if hidden:
            try:
                subprocess.check_call(['attrib', '+h', 'key.key'])
            except:
                print('key.key cannot be hidden')


    # TODO falta comprobar que deba ponerse en visible antes
    def load_key_from_file(self):
        return open("key.key", "rb").read()

    
    # TODO aqui pone test.txt a visible antes. Falta comprobar que deba ponerse en visible antes
    """
    @resumen: Devuelve true si la clave que se pasa por argumento puede desencriptar el archivo oculto. test.txt es de gran importancia no puede borrarse asi como asi
    Tambien establece la clave o key una vez se ha comprobado que es la correcta
    """
    def correct_key(self, key):
        print('Hey checking the key')
        aux = Fernet(key)
        try:
            subprocess.check_call(['attrib', '-h', 'test.txt']) # comentar en caso de que no haga falta hacerlo visible
        except:
            print('error in -h')
        with open('test.txt', 'rb') as test_file:
            data = test_file.read()

        try:
            decrypted = aux.decrypt(data)
            self.key = self.set_key(key)
            return True
        except Exception as e:
            print(e)
            return False

            
    def symmetric_encrypt_or_decrypt(self, full_path, opt='encrypt'):
        try:
            data = self.load_data(full_path)
            if opt == 'encrypt':
                encrypted_data = self.fernet.encrypt(data)
                self.save_data(full_path, encrypted_data)
            elif opt == 'decrypt':
                decrypted_data = self.fernet.decrypt(data)
                self.save_data(full_path, decrypted_data, opt='del_ext')
            else:
                raise ValueError('Invalid argument on encryption/decryption')
        except ValueError as ve:
            print(ve)
        except PermissionError as pe:
            print(pe)
        except IOError as ioe:
            print(ioe)

