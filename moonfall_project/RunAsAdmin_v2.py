#https://stackoverflow.com/questions/19672352/how-to-run-python-script-with-elevated-privilege-on-windows
import os
import sys
import win32com.shell.shell as shell
ASADMIN = 'asadmin'

import ctypes
 
def isAdmin():
    try:
        is_admin = (os.getuid() == 0)
    except AttributeError:
        is_admin = ctypes.windll.shell32.IsUserAnAdmin() != 0
    return is_admin

print(sys.argv[-1])
if sys.argv[-1] != ASADMIN:
    print('HOLA')
    script = os.path.abspath(sys.argv[0])
    params = ' '.join([script] + sys.argv[1:] + [ASADMIN])
    shell.ShellExecuteEx(lpVerb='runas', lpFile=sys.executable, lpParameters=params)
    print(isAdmin())
    sys.exit(0)

with open("somefilename.txt", "w") as out:
    out.write("i am root")
