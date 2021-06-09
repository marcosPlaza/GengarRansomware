import base64
from cryptography.fernet import Fernet

class KeyManager():
    def __init__(self, key_bytes=None):
        if key_bytes is not None:
            self.key_bytes = key_bytes
            self.encrypted_key = base64.b64encode(str(key_bytes).encode("ascii")).decode("ascii")
            self.decrypted_key = bytes(base64.b64decode(self.encrypted_key.encode("ascii")).decode("ascii")[2:-1], 'utf-8')

    def encrypt_base64(self,key):
        return base64.b64encode(str(key).encode("ascii")).decode("ascii")

    def decrypt_base64(self,key):
        return bytes(base64.b64decode(str(key).encode("ascii")).decode("ascii")[2:-1], 'utf-8')

# 
if __name__ == "__main__":
    key = Fernet.generate_key()
    f = Fernet(key)

    print(key)
    print(type(key))

    byte_word = b"Hola me llamo marcos"
    encrypted_word = f.encrypt(byte_word)

    print(encrypted_word)

    km = KeyManager()
    enc_key = km.encrypt_base64(key)

    dec_key = km.decrypt_base64(enc_key)

    print(dec_key)
    print(type(dec_key))


    f2 = Fernet(dec_key)
    
    decrypted_word = f2.decrypt(encrypted_word)

    print(decrypted_word)




