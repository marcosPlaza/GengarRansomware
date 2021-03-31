import ctypes
import sys
import os
import traceback

CMD_PATH = "C:\\Windows\\System32\\cmd.exe"
EXEC_PATH = "C:\\Users\\marco\\OneDrive\\Escritorio\\ransomware\\moonfall_project\\dist\\test.exe"

class Launcher:
    def run_exe_as_admin(self, executable=None, argv=None, debug=False):
        if executable is None: executable = sys.executable # testing with python

        if hasattr(sys, '_MEIPASS'): argv = argv[1:]

        if debug:print('Command line: ', executable, argv)
        ret = ctypes.windll.shell32.ShellExecuteW(None, u"runas", executable, argv, None, 1)

        if ret <= 32: raise Exception(".exe file cannot be executed")


if __name__ == "__main__":
    launcher = Launcher()
    try:
        launcher.run_exe_as_admin(argv="TaskManager.py", debug=True)
    except Exception as e:
        print(e)
        traceback.print_exc()