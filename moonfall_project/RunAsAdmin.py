# class adapted from https://gist.github.com/GaryLee/d1cf2089c3a515691919
import sys
import ctypes

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
        argument_line = u' '.join(arguments)
        executable = str(sys.executable)
        if debug:
            print('Command line: ', executable, argument_line)
        ret = shell32.ShellExecuteW(None, u"runas", executable, argument_line, None, 1)
        if int(ret) <= 32:
            return False
        return None
    

if __name__ == '__main__':
    raa = RunAsAdmin()
    ret = raa.run_as_admin()
    if ret is True:
        print('I have admin privilege.')
        input('Press ENTER to exit.')
    elif ret is None:
        print('I am elevating to admin privilege.')
        input('Press ENTER to exit.')
    else:
        print('Error(ret=%d): cannot elevate privilege.' % (ret, ))