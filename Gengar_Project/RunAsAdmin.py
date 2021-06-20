# class adapted from https://gist.github.com/GaryLee/d1cf2089c3a515691919
import sys
import ctypes
import os
import traceback
# NOT USED
class RunAsAdmin():
    # returning true if script is executing as admin
    def isAdmin(self):
        if os.name == 'nt':
            try:
                return ctypes.windll.shell32.IsUserAnAdmin() == 1
            except:
                traceback.print_exc()
                return False
        else:
            raise Exception("Not running in Windows System")

    # TODO
    def run_as_admin(self, argv=None, debug=False):
        shell32 = ctypes.windll.shell32

        if argv is None and shell32.IsUserAnAdmin():
            return True
            
        if argv is None:
            argv = sys.argv
        
        if hasattr(sys, '_MEIPASS'):
            # Support pyinstaller wrapped program.
            arguments = map(str, argv[1:])
        else:
            arguments = map(str, argv)
            print(argv)
            arguments2 = str(argv)
            print(arguments2)

        argument_line = u' '.join(arguments)
        executable = str(sys.executable)

        if debug:
            print('Command line: ', executable, arguments2)

        ret = shell32.ShellExecuteW(None, u"runas", executable, arguments2, None, 1)

        if int(ret) <= 32:
            return False
        return None


if __name__ == '__main__':
    raa = RunAsAdmin()
    ret = raa.run_as_admin(argv="test.py", debug=True)
    if ret is True:
        print('I have admin privilege.')
        input('Press ENTER to exit.')
    elif ret is None:
        print('I am elevating to admin privilege.')
        input('Press ENTER to exit.')
    else:
        print('Error(ret=%d): cannot elevate privilege.' % (ret, ))
