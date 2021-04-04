import winreg
import os
import re
import time

"""
Check here - https://resources.infosecinstitute.com/topic/malware-anti-analysis-techniques-ways-bypass/
https://www.goggleheadedhacker.com/blog/post/23
Techniques
Check registry entry
Check if registry exists
Check if some file exists
"""
class VirtualEnvironmentDetector:
    LOCATION_1 = "SYSTEM\\ControlSet001\\Control\\Class\\{4d36e965-e325-11ce-bfc1-08002be10318}\\0000\\DriverDesc"  # If registry exists
    LOCATION_2 = "SYSTEM\\ControlSet001\\Control\\Class\\{4d36e965-e325-11ce-bfc1-08002be10318}\\0000\\ProviderName"  # If registry exists
    LOCATION_3 = "HARDWARE\\DEVICEMAP\\Scsi\\Scsi Port 0\\Scsi Bus 0\\Target Id 0\\Logical Unit Id 0\\Identifier" # Find QEMU or VBOX or VMWare
    LOCATION_4 = "HARDWARE\\Description\\System\\SystemBiosVersion" # Find QEMU or VBOX
    LOCATION_5 = "HARDWARE\\Description\\System\\VideoBiosVersion" # Find VIRTUALBOX
    LOCATION_6 = "SOFTWARE\\Oracle\\VirtualBox Guest Additions" # If registry exists
    LOCATION_7 = "WINDOWS\\system32\\drivers\\VBoxMouse.sys" # Check if file driver exists
    LOCATION_8 = "SOFTWARE\\VMware, Inc.\\VMware Tools" # If registry exists
    LOCATION_12 = "HARDWARE\\ACPI\\FADT\\VBOX__" # Check if reg key exists

    re_1 = "^([0-9A-Fa-f]){60,60}$" # to check 60 random hex values
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

    OTHER_REGEX = [ "c\:\\\\sample\.exe$", "c\:\\\\InsideTm\\\\.*"]

    def __init__(self, enable_detection = True):
        if enable_detection:
            #full file detection
            self.general = self.file_or_dir_detection(self.GENERAL_FILES)
            self.parallels = self.file_or_dir_detection(self.PARALLELS_FILES)
            self.virtualbox = self.file_or_dir_detection(self.VIRTUALBOX_FILES)
            self.virtualpc = self.file_or_dir_detection(self.VIRTUALPC_FILES)
            self.vmware = self.file_or_dir_detection(self.VMWARE_FILES)
        else:
            print("DEBUG MODE ENABLED")

    def print_check_results(self):
        print("General ", self.general)
        print("Parallels ", self.parallels)
        print("Virtual Box ", self.virtualbox)
        print("Virtual PC ", self.virtualpc)
        print("VMWare ", self.vmware)

    def file_or_dir_detection(self, names_list):
        for fod in names_list:
            if os.path.exists(fod): return True
        return False
        
    def check_registries_exists(self, reg_path):
        # Try to read the key
        try:
            reg = winreg.OpenKeyEx(winreg.HKEY_LOCAL_MACHINE, reg_path)
            print(reg)
            winreg.CloseKey(reg)
            return True
        except FileNotFoundError as fnfe:
            return False

    def check_registry_value(self, reg_path):
        pass
        

    # IDT address
    
if __name__ == "__main__":
    start_time = time.time()
    ved = VirtualEnvironmentDetector()
    ved.print_check_results()
    print("--- %s seconds ---" % (time.time() - start_time))