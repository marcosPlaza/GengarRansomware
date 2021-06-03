import winreg
import win32api
import os
import re
import time
import uuid
import traceback
import psutil

# TODO Not tested

"""
Check here - https://resources.infosecinstitute.com/topic/malware-anti-analysis-techniques-ways-bypass/
https://www.goggleheadedhacker.com/blog/post/23
Techniques
Check registry entry
Check if registry exists
Check if some file exists
"""
# TODO be careful with projects like this pls: https://github.com/fr0gger/RocProtect-V1
# Asignar una ponderación para cada una de las pruebas
class VirtualEnvironmentDetector:
    # PHASE 1 - CHECK IF FILES/DIRECTORIES EXISTS
    re_1 = "^([0-9A-Fa-f]){60,60}$" # to check 60 random hex values  # NOT USED YET
    GENERAL_FILES = ["c:\\take_screenshot.ps1", "c:\\loaddll.exe", "c:\\email.doc", "c:\\email.htm", "c:\\123\\email.doc",
     "c:\\123\\email.docx", "c:\\a\\foobar.bmp", "c:\\a\\foobar.doc", "c:\\a\\foobar.gif", "c:\\symbols\\aagmmc.pdb"]

    PARALLELS_FILES = ["c:\\windows\\system32\\drivers\\prleth.sys", "c:\\windows\\system32\\drivers\\prlfs.sys", "c:\\windows\\system32\\drivers\\prlmouse.sys", "c:\\windows\\system32\\drivers\\prlvideo.sys",
    "c:\\windows\\system32\\drivers\\prltime.sys", "c:\\windows\\system32\\drivers\\prl_pv32.sys", "c:\\windows\\system32\\drivers\\prl_paravirt_32.sys"]

    VIRTUALBOX_FILES = ["c:\\windows\\system32\\drivers\\VBoxMouse.sys", "c:\\windows\\system32\\drivers\\VBoxGuest.sys", "c:\\windows\\system32\\drivers\\VBoxSF.sys", "c:\\windows\\system32\\drivers\\VBoxVideo.sys",
    "c:\\windows\\system32\\vboxdisp.dll", "c:\\windows\\system32\\vboxhook.dll", "c:\\windows\\system32\\vboxmrxnp.dll", "c:\\windows\\system32\\vboxogl.dll", "c:\\windows\\system32\\vboxoglarrayspu.dll", "c:\\windows\\system32\\vboxoglcrutil.dll",
    "c:\\windows\\system32\\vboxoglerrorspu.dll", "c:\\windows\\system32\\vboxoglfeedbackspu.dll", "c:\\windows\\system32\\vboxoglpackspu.dll", "c:\\windows\\system32\\vboxoglpassthroughspu.dll", "c:\\windows\\system32\\vboxservice.exe",
    "c:\\windows\\system32\\vboxtray.exe", "c:\\windows\\system32\\VBoxControl.exe"]

    VIRTUALPC_FILES = ["c:\\windows\\system32\\drivers\\vmsrvc.sys", "c:\\windows\\system32\\drivers\\vpc-s3.sys"]

    VMWARE_FILES = ["c:\\windows\\system32\\drivers\\vmmouse.sys", "c:\\windows\\system32\\drivers\\vmnet.sys", "c:\\windows\\system32\\drivers\\vmxnet.sys", "c:\\windows\\system32\\drivers\\vmhgfs.sys",
    "c:\\windows\\system32\\drivers\\vmx86.sys", "c:\\windows\\system32\\drivers\\hgfs.sys"]

    GENERAL_DIRS = ["c:\\analysis", "%PROGRAMFILES%\\oracle\\virtualbox guest additions\\", "%PROGRAMFILES%\\VMware\\"]

    OTHER_REGEX = ["c\:\\\\sample\.exe$", "c\:\\\\InsideTm\\\\.*"] # NOT USED YET - REGEX

    # PHASE 2 - CHECK IF REGISTRY ENTRIES EXISTS
    GENERAL_REGS = ["HKLM\\Software\\Classes\\Folder\\shell\\sandbox"] 

    HYPER_V_REGS = ["HKLM\\SOFTWARE\\Microsoft\\Hyper-V", "HKLM\\SOFTWARE\\Microsoft\\VirtualMachine", "HKLM\\SOFTWARE\\Microsoft\\Virtual Machine\\Guest\\Parameters", "HKLM\\SYSTEM\\ControlSet001\\Services\\vmicheartbeat",
    "HKLM\\SYSTEM\\ControlSet001\\Services\\vmicvss", "HKLM\\SYSTEM\\ControlSet001\\Services\\vmicshutdown", "HKLM\\SYSTEM\\ControlSet001\\Services\\vmicshutdown", "HKLM\\SYSTEM\\ControlSet001\\Services\\vmicexchange"]

    PARALLELS_REGS = ["HKLM\\SYSTEM\\CurrentControlSet\\Enum\\PCI\\VEN_1AB8*"] # "VEN_XXXX&DEV_YYYY&SUBSYS_ZZZZ&REV_WW" - REGEX

    SANDBOXIE_REGS = ["HKLM\\SYSTEM\\CurrentControlSet\\Services\\SbieDrv", "HKLM\\SOFTWARE\\Microsoft\\Windows\\CurrentVersion\\Uninstall\\Sandboxie"]

    VIRTUALBOX_REGEX = "HKLM\\SYSTEM\\CurrentControlSet\\Enum\\PCI\\VEN_80EE*" # REGEX

    VIRTUALBOX_REGS =["HKLM\\HARDWARE\\ACPI\\DSDT\\VBOX__", "HKLM\\HARDWARE\\ACPI\\FADT\\VBOX__", "HKLM\\HARDWARE\\ACPI\\RSDT\\VBOX__", "HKLM\\SOFTWARE\\Oracle\\VirtualBox Guest Additions",
    "HKLM\\SYSTEM\\ControlSet001\\Services\\VBoxGuest", "HKLM\\SYSTEM\\ControlSet001\\Services\\VBoxMouse", "HKLM\\SYSTEM\\ControlSet001\\Services\\VBoxService", "HKLM\\SYSTEM\\ControlSet001\\Services\\VBoxSF", "HKLM\\SYSTEM\\ControlSet001\\Services\\VBoxVideo"]

    VIRTUALPC_REGEX = "HKLM\\SYSTEM\\CurrentControlSet\\Enum\\PCI\\VEN_5333*" # REGEX
    VIRTUALPC_REGS = ["HKLM\\SYSTEM\\ControlSet001\\Services\\vpcbus", "HKLM\\SYSTEM\\ControlSet001\\Services\\vpc-s3", "HKLM\\SYSTEM\\ControlSet001\\Services\\vpcuhub", "HKLM\\SYSTEM\\ControlSet001\\Services\\msvmmouf"]

    VMWARE_REGS = ["HKLM\\SYSTEM\\CurrentControlSet\\Enum\\PCI\\VEN_15AD*", "HKCU\\SOFTWARE\\VMware, Inc.\\VMware Tools", "HKLM\\SOFTWARE\\VMware, Inc.\\VMware Tools", "HKLM\\SYSTEM\\ControlSet001\\Services\\vmdebug", "HKLM\\SYSTEM\\ControlSet001\\Services\\vmmouse",
     "HKLM\\SYSTEM\\ControlSet001\\Services\\VMTools", "HKLM\\SYSTEM\\ControlSet001\\Services\\VMMEMCTL", "HKLM\\SYSTEM\\ControlSet001\\Services\\vmware", "HKLM\\SYSTEM\\ControlSet001\\Services\\vmci", "HKLM\\SYSTEM\\ControlSet001\\Services\\vmx86", "HKLM\\SYSTEM\\CurrentControlSet\\Enum\\IDE\\CdRomNECVMWar_VMware_IDE_CD*", 
     "HKLM\\SYSTEM\\CurrentControlSet\\Enum\\IDE\\CdRomNECVMWar_VMware_SATA_CD*", "HKLM\\SYSTEM\\CurrentControlSet\\Enum\\IDE\\DiskVMware_Virtual_IDE_Hard_Drive*", "HKLM\\SYSTEM\\CurrentControlSet\\Enum\\IDE\\DiskVMware_Virtual_SATA_Hard_Drive*"]

    WINE_REGS = ["HKCU\\SOFTWARE\\Wine", "HKLM\\SOFTWARE\\Wine"]

    XEN_REGS = ["HKLM\\HARDWARE\\ACPI\\DSDT\\xen", "HKLM\\HARDWARE\\ACPI\\FADT\\xen", "HKLM\\HARDWARE\\ACPI\\RSDT\\xen", "HKLM\\SYSTEM\\ControlSet001\\Services\\xenevtchn", "HKLM\\SYSTEM\\ControlSet001\\Services\\xennet", "HKLM\\SYSTEM\\ControlSet001\\Services\\xennet6", "HKLM\\SYSTEM\\ControlSet001\\Services\\xensvc", "HKLM\\SYSTEM\\ControlSet001\\Services\\xenvdb"]

    SUBKEY_REGEX = "VEN_XXXX&DEV_YYYY&SUBSYS_ZZZZ&REV_WW"

    # PHASE 3 - CHECK IF REGISTRY ENTRIES RETURN THE EXPECTED VALUE
    # INSERT HERE

    # PHASE 4 - CHECK NETWORK ADDRESSES
    def __init__(self, file_detection = True, registry_detection = True):
        if file_detection:
            #full file detection
            self.general_files = self.file_or_dir_detection(self.GENERAL_FILES)
            self.parallels_files = self.file_or_dir_detection(self.PARALLELS_FILES)
            self.virtualbox_files = self.file_or_dir_detection(self.VIRTUALBOX_FILES)
            self.virtualpc_files = self.file_or_dir_detection(self.VIRTUALPC_FILES)
            self.vmware_files = self.file_or_dir_detection(self.VMWARE_FILES)
        
        # Not tested
        if registry_detection:
            self.general_regs = self.check_registries_exists(self.GENERAL_REGS)
            self.hyperv_regs = self.check_registries_exists(self.HYPER_V_REGS)
            self.parallels_regs = self.check_registries_exists(self.PARALLELS_REGS)
            self.sandboxie_regs = self.check_registries_exists(self.SANDBOXIE_REGS)
            self.virtualbox_regs = self.check_registries_exists(self.VIRTUALBOX_REGS)
            self.virtualpc_regs = self.check_registries_exists(self.VIRTUALPC_REGS)
            self.vmware_regs = self.check_registries_exists(self.VMWARE_REGS)
            self.wine_regs = self.check_registries_exists(self.WINE_REGS)
            self.xen_regs = self.check_registries_exists(self.XEN_REGS)
        

    def print_check_results(self):
        print("General files", self.general_files)
        print("Parallels files", self.parallels_files)
        print("Virtual Box files", self.virtualbox_files)
        print("Virtual PC files", self.virtualpc_files)
        print("VMWare files", self.vmware_files)

        print("General regs", self.general_regs)
        print("Hyper V regs", self.hyperv_regs)
        print("Parallels regs", self.parallels_regs)
        print("Sandboxie regs", self.sandboxie_regs)
        print("Virtual Box regs", self.virtualbox_regs)
        print("Virtual PC regs", self.virtualpc_regs)
        print("VMWare regs", self.vmware_regs)
        print("Wine regs", self.wine_regs)
        print("Xen regs", self.xen_regs)

    def file_or_dir_detection(self, names_list):
        for fod in names_list:
            if os.path.exists(fod): return True
        return False
    
    def check_registries_exists(self, regs_list):
        for reg in regs_list:
            if self.check_registry_exists(reg, debug=False): return True
        return False

    def check_registry_exists(self, reg_path, debug=True):
        # Try to read the key
        try:
            reg = winreg.OpenKeyEx(winreg.HKEY_LOCAL_MACHINE, reg_path)
            if debug: print(reg)
            winreg.CloseKey(reg)
            return True
        except FileNotFoundError as fnfe:
            
            return False

    def check_registry_value(self, reg_path):
        pass
        
    # NOT TESTED
    """ Returns: True if running in a Docker container """
    def in_docker(self):
        with open('/proc/1/cgroup', 'rt') as ifh:
            return 'docker' in ifh.read()

    # Cual es el determinante de si es un entorno virtualizado para el numero de cpus?
    def check_num_processors(self):
        try:
            return psutil.cpu_count()
        except:
            pass

    def get_ram_size(self):
        try:
            bytes = psutil.virtual_memory()
            return bytes.total / 1e9
        except:
            traceback.print_exc()

    def get_screen_res(self):
        try:
            return (win32api.GetSystemMetrics(0), win32api.GetSystemMetrics(1))
        except:
            traceback.print_exc()

    def get_harddrive_size(self, free_space=False):
        try:
            hdd = psutil.disk_usage('/')
            if free_space:
                return hdd.free / 1e9
            return hdd.total / 1e9
        except:
            traceback.print_exc()
    
    
    
if __name__ == "__main__":
    start_time = time.time()
    ved = VirtualEnvironmentDetector()
    ved.print_check_results()
    print("--- %s seconds ---" % (time.time() - start_time))
    print(ved.check_num_processors()) # prints 12 for amd ryzen 5 5600 X
    print(ved.get_ram_size())
    print(ved.get_screen_res())
    print(ved.get_harddrive_size())
    input("ENTER to exit.")
