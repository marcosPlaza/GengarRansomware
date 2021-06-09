from cryptography.fernet import Fernet
import subprocess
import Utils
import oschmod
import traceback

# TODO traceback using needed
# TODO test in different size and type of files
class CryptoManager(Utils):
    def __init__(self, key=None, action='decrypt'):
        if key is None:
            self.key = Fernet.generate_key()
        else:
            self.key = key
            
        self.fernet = Fernet(self.key)
        
        if action == 'encrypt':
            msg = str.encode('This is a test file that may be hidden')
            enc_msg = self.fernet.encrypt(msg)
            
            try:
                subprocess.check_call(['attrib', '-h', 'test.txt'])
            except Exception:
                print('test.txt cannot revealed')
                traceback.print_exc()
                
            with open('test.txt', 'wb') as test_file:
                test_file.write(enc_msg)
                
            try:
                subprocess.check_call(['attrib', '+h', 'test.txt'])
            except Exception:
                print('test.txt cannot be hidden')
                traceback.print_exc()

        
    def set_key(self, key):
        self.key = key
        
        
    def set_fernet(self, _fernet):
        self.fernet = _fernet


    def save_key_as_file(self, hidden=True):
        try:
            subprocess.check_call(['attrib', '-h', 'key.key'])
        except:
            print('key.key cannot revealed')
                
        with open('key.key', 'wb') as key_file:
            key_file.write(self.key)

        if hidden:
            try:
                subprocess.check_call(['attrib', '+h', 'key.key'])
            except:
                print('key.key cannot be hidden')


    def load_key_from_file(self):
        try:
            subprocess.check_call(['attrib', '-h', 'key.key'])
        except:
            print('error in -h')
            
        return open("key.key", "rb").read()

    
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
            self.set_key(key)
            self.set_fernet(aux)
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
        except Exception as e:
            print('Something on the encryption failed')
            print(e)

