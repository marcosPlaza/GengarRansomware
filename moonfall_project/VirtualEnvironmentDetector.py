import winreg
import win32api
import os
import re
import time
import uuid
import traceback
import psutil

class VirtualEnvironmentDetector:
    # CHECK IF FILES/DIRECTORIES EXISTS
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

    # CHECK IF REGISTRY ENTRIES EXISTS
    GENERAL_REGS = ["HKLM\\Software\\Classes\\Folder\\shell\\sandbox"] 
    HYPER_V_REGS = ["HKLM\\SOFTWARE\\Microsoft\\Hyper-V", "HKLM\\SOFTWARE\\Microsoft\\VirtualMachine", "HKLM\\SOFTWARE\\Microsoft\\Virtual Machine\\Guest\\Parameters", "HKLM\\SYSTEM\\ControlSet001\\Services\\vmicheartbeat",
    "HKLM\\SYSTEM\\ControlSet001\\Services\\vmicvss", "HKLM\\SYSTEM\\ControlSet001\\Services\\vmicshutdown", "HKLM\\SYSTEM\\ControlSet001\\Services\\vmicshutdown", "HKLM\\SYSTEM\\ControlSet001\\Services\\vmicexchange"]
    PARALLELS_REGS = ["HKLM\\SYSTEM\\CurrentControlSet\\Enum\\PCI\\VEN_1AB8*"]
    SANDBOXIE_REGS = ["HKLM\\SYSTEM\\CurrentControlSet\\Services\\SbieDrv", "HKLM\\SOFTWARE\\Microsoft\\Windows\\CurrentVersion\\Uninstall\\Sandboxie"]
    VIRTUALBOX_REGS =["HKLM\\HARDWARE\\ACPI\\DSDT\\VBOX__", "HKLM\\HARDWARE\\ACPI\\FADT\\VBOX__", "HKLM\\HARDWARE\\ACPI\\RSDT\\VBOX__", "HKLM\\SOFTWARE\\Oracle\\VirtualBox Guest Additions",
    "HKLM\\SYSTEM\\ControlSet001\\Services\\VBoxGuest", "HKLM\\SYSTEM\\ControlSet001\\Services\\VBoxMouse", "HKLM\\SYSTEM\\ControlSet001\\Services\\VBoxService", "HKLM\\SYSTEM\\ControlSet001\\Services\\VBoxSF", "HKLM\\SYSTEM\\ControlSet001\\Services\\VBoxVideo"]
    VIRTUALPC_REGS = ["HKLM\\SYSTEM\\ControlSet001\\Services\\vpcbus", "HKLM\\SYSTEM\\ControlSet001\\Services\\vpc-s3", "HKLM\\SYSTEM\\ControlSet001\\Services\\vpcuhub", "HKLM\\SYSTEM\\ControlSet001\\Services\\msvmmouf"]
    VMWARE_REGS = ["HKLM\\SYSTEM\\CurrentControlSet\\Enum\\PCI\\VEN_15AD*", "HKCU\\SOFTWARE\\VMware, Inc.\\VMware Tools", "HKLM\\SOFTWARE\\VMware, Inc.\\VMware Tools", "HKLM\\SYSTEM\\ControlSet001\\Services\\vmdebug", "HKLM\\SYSTEM\\ControlSet001\\Services\\vmmouse",
     "HKLM\\SYSTEM\\ControlSet001\\Services\\VMTools", "HKLM\\SYSTEM\\ControlSet001\\Services\\VMMEMCTL", "HKLM\\SYSTEM\\ControlSet001\\Services\\vmware", "HKLM\\SYSTEM\\ControlSet001\\Services\\vmci", "HKLM\\SYSTEM\\ControlSet001\\Services\\vmx86", "HKLM\\SYSTEM\\CurrentControlSet\\Enum\\IDE\\CdRomNECVMWar_VMware_IDE_CD*", 
     "HKLM\\SYSTEM\\CurrentControlSet\\Enum\\IDE\\CdRomNECVMWar_VMware_SATA_CD*", "HKLM\\SYSTEM\\CurrentControlSet\\Enum\\IDE\\DiskVMware_Virtual_IDE_Hard_Drive*", "HKLM\\SYSTEM\\CurrentControlSet\\Enum\\IDE\\DiskVMware_Virtual_SATA_Hard_Drive*"]
    WINE_REGS = ["HKCU\\SOFTWARE\\Wine", "HKLM\\SOFTWARE\\Wine"]
    XEN_REGS = ["HKLM\\HARDWARE\\ACPI\\DSDT\\xen", "HKLM\\HARDWARE\\ACPI\\FADT\\xen", "HKLM\\HARDWARE\\ACPI\\RSDT\\xen", "HKLM\\SYSTEM\\ControlSet001\\Services\\xenevtchn", "HKLM\\SYSTEM\\ControlSet001\\Services\\xennet", "HKLM\\SYSTEM\\ControlSet001\\Services\\xennet6", "HKLM\\SYSTEM\\ControlSet001\\Services\\xensvc", "HKLM\\SYSTEM\\ControlSet001\\Services\\xenvdb"]

    # CHECK IF REGISTRY ENTRIES RETURN THE EXPECTED VALUE
    GENERAL_KEYVAL =[("HKLM\\HARDWARE\\Description\\System", "SystemBiosDate", "06/23/99"), ("HKLM\\HARDWARE\\Description\\System\\BIOS", "SystemProductName", "A M I")]
    BOCHS_KEYVAL =[("HKLM\\HARDWARE\\Description\\System", "SystemBiosVersion", "BOCHS"), ("HKLM\\HARDWARE\\Description\\System", "VideoBiosVersion", "BOCHS")]
    
    # NOT USED YET
    ANUBIS_KEYVAL =[("HKLM\\SOFTWARE\\Microsoft\\Windows\\CurrentVersion", "ProductID", "76487-337-8429955-22614"), ("HKLM\\SOFTWARE\\Microsoft\\Windows NT\\CurrentVersion", "ProductID", "76487-337-8429955-22614")]
    CWSANDBOX_KEYVAL =[("HKLM\\SOFTWARE\\Microsoft\\Windows\\CurrentVersion", "ProductID", "76487-644-3177037-23510"), ("HKLM\\SOFTWARE\\Microsoft\\Windows NT\\CurrentVersion", "ProductID", "76487-644-3177037-23510")]
    JOEBOX_KEYVAL =[("HKLM\\SOFTWARE\\Microsoft\\Windows\\CurrentVersion", "ProductID", "55274-640-2673064-23950"), ("HKLM\\SOFTWARE\\Microsoft\\Windows NT\\CurrentVersion", "ProductID", "55274-640-2673064-23950")]
    
    PARALLELS_KEYVAL =[("HKLM\\HARDWARE\\Description\\System", "SystemBiosVersion", "PARALLELS"), ("HKLM\\HARDWARE\\Description\\System", "VideoBiosVersion", "PARALLELS")]
    QEMU_KEYVAL = [("HKLM\\HARDWARE\\Description\\System", "SystemBiosVersion", "QEMU"),("HKLM\\HARDWARE\\Description\\System", "VideoBiosVersion", "QEMU"), ("HKLM\\HARDWARE\\Description\\System\\BIOS", "SystemManufacturer", "QEMU")]
    VIRTUALBOX_KEYVAL = [("HKLM\\HARDWARE\\Description\\System", "SystemBiosVersion", "VBOX"), ("HKLM\\HARDWARE\\Description\\System", "VideoBiosVersion", "VIRTUALBOX"), ("HKLM\\HARDWARE\\Description\\System\\BIOS", "SystemProductName", "VIRTUAL"), ("HKLM\\SYSTEM\\ControlSet001\\Services\\Disk\\Enum", "DeviceDesc", "VBOX"),
    ("HKLM\\SYSTEM\\ControlSet001\\Services\\Disk\\Enum", "FriendlyName", "VBOX"), ("HKLM\\SYSTEM\\ControlSet002\\Services\\Disk\\Enum", "DeviceDesc", "VBOX"), ("HKLM\\SYSTEM\\ControlSet002\\Services\\Disk\\Enum", "FriendlyName", "VBOX"), ("HKLM\\SYSTEM\\ControlSet003\\Services\\Disk\\Enum", "DeviceDesc", "VBOX"), ("HKLM\\SYSTEM\\ControlSet003\\Services\\Disk\\Enum", "FriendlyName", "VBOX"),
    ("HKLM\\SYSTEM\\CurrentControlSet\\Control\\SystemInformation", "SystemProductName", "VIRTUAL"), ("HKLM\\SYSTEM\\CurrentControlSet\\Control\\SystemInformation", "SystemProductName", "VIRTUALBOX")]
    VMWARE_KEYVAL = [("HKLM\\HARDWARE\\Description\\System", "SystemBiosVersion", "VMWARE"), ("HKLM\HARDWARE\Description\System", "SystemBiosVersion", "INTEL - 6040000"), ("HKLM\\HARDWARE\\Description\\System", "VideoBiosVersion", "VMWARE"), ("HKLM\\HARDWARE\\Description\\System\\BIOS", "SystemProductName", "VMware"),
    ("HKLM\\SYSTEM\\ControlSet001\\Services\\Disk\\Enum", "0", "VMware"), ("HKLM\\SYSTEM\\ControlSet001\\Services\\Disk\\Enum", "1", "VMware"), ("HKLM\\SYSTEM\\ControlSet001\\Services\\Disk\\Enum", "DeviceDesc", "VMware"), ("HKLM\\SYSTEM\\ControlSet001\\Services\\Disk\\Enum", "FriendlyName", "VMware"), ("HKLM\\SYSTEM\\ControlSet002\\Services\\Disk\\Enum", "DeviceDesc", "VMware"),
    ("HKLM\\SYSTEM\\ControlSet002\\Services\\Disk\\Enum", "FriendlyName", "VMware"), ("HKLM\\SYSTEM\\ControlSet003\\Services\\Disk\\Enum", "DeviceDesc", "VMware"), ("HKLM\\SYSTEM\\ControlSet003\\Services\\Disk\\Enum", "FriendlyName", "VMware"),
    ("HKCR\\Installer\\Products", "ProductName", "vmware tools"), ("HKCU\\SOFTWARE\\Microsoft\\Windows\\CurrentVersion\\Uninstall", "DisplayName", "vmware tools"),  ("HKLM\\SOFTWARE\\Microsoft\\Windows\\CurrentVersion\\Uninstall", "DisplayName", "vmware tools"), ("HKLM\\SYSTEM\\CurrentControlSet\\Control\\SystemInformation", "SystemProductName", "VMWARE")]
    XEN_KEYVAL = [("HKLM\\HARDWARE\\Description\\System\\BIOS", "SystemProductName", "Xen")]

    # CHECK MAC ADDRESS TO IDENTIFY VM
    PARALLELS_MAC = ["00:1C:42"]
    VIRTUALBOX_MAC = ["08:00:27"]
    VMWARE_MAC = ["00:05:69", "00:0C:29", "00:1C:14", "00:50:56"]
    XEN_MAC = ["00:16:E3"]


    def __init__(self, file_detection = True, registry_detection = True, registry_string=True, os_features=True, check_docker=True, check_mac_address=True, dodelay=True, delay=5*60):
        if file_detection:
            self.general_files = self.file_or_dir_detection(self.GENERAL_FILES)
            self.parallels_files = self.file_or_dir_detection(self.PARALLELS_FILES)
            self.virtualbox_files = self.file_or_dir_detection(self.VIRTUALBOX_FILES)
            self.virtualpc_files = self.file_or_dir_detection(self.VIRTUALPC_FILES)
            self.vmware_files = self.file_or_dir_detection(self.VMWARE_FILES)
        
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

        if registry_string:
            self.general_regs_string = self.check_string_in_registries(self.GENERAL_KEYVAL)
            self.bochs_regs_string = self.check_string_in_registries(self.BOCHS_KEYVAL)
            self.parallels_regs_string = self.check_string_in_registries(self.PARALLELS_KEYVAL)
            self.qemu_regs_string = self.check_string_in_registries(self.QEMU_KEYVAL)
            self.virtualbox_regs_string = self.check_string_in_registries(self.VIRTUALBOX_KEYVAL)
            self.vmware_regs_string = self.check_string_in_registries(self.VMWARE_KEYVAL)
            self.xen_regs_string = self.check_string_in_registries(self.XEN_KEYVAL)

        # CHECK OS FEATURES; IF NUMBER OF PROCESSORS IS LOWER THAN 2 OR RAM SIZE IS LOW THEN CANCEL
        if os_features:
            self.num_processors = self.check_num_processors() < 2
            self.ram_size = self.get_ram_size() < 4096
            # NOT CHECKING SCREEN RESOLUTION

        # CHECK IF THE PROGRAMM IS RUNNING IN DOCKER CONTAINER
        if check_docker:
            self.is_docker = self.in_docker()

        if check_mac_address:
            self.parallel_mac = self.check_mac_address_bylist(self.PARALLELS_MAC)
            self.virtualbox_mac = self.check_mac_address_bylist(self.VIRTUALBOX_MAC)
            self.vmware_mac = self.check_mac_address_bylist(self.VMWARE_MAC)
            self.xen_mac = self.check_mac_address_bylist(self.XEN_MAC)

        # CHECK IF WE ARE RUNNING ON CUCKOO SANDBOX
        if dodelay:
            self.activity_stopped = self.delay_anti_cuckoo(0)

    def print_check_results(self, file_detection = True, registry_detection = True, registry_string=True, os_features=True, check_docker=True, check_mac_address=True, dodelay=True, delay=5*60):
        print("General files -->", self.general_files)
        print("Parallels files -->", self.parallels_files)
        print("Virtual Box files -->", self.virtualbox_files)
        print("Virtual PC files -->", self.virtualpc_files)
        print("VMWare files -->", self.vmware_files)

        print("General regs -->", self.general_regs)
        print("Hyper V regs -->", self.hyperv_regs)
        print("Parallels regs -->", self.parallels_regs)
        print("Sandboxie regs -->", self.sandboxie_regs)
        print("Virtual Box regs -->", self.virtualbox_regs)
        print("Virtual PC regs -->", self.virtualpc_regs)
        print("VMWare regs -->", self.vmware_regs)
        print("Wine regs -->", self.wine_regs)
        print("Xen regs -->", self.xen_regs)

        print("General regs string -->", self.general_regs_string)
        print("Bochs regs string -->", self.bochs_regs_string)
        print("Parallels regs string -->", self.parallels_regs_string)
        print("Qemu regs string -->", self.qemu_regs_string)
        print("Virtual Box regs string -->", self.virtualbox_regs_string)
        print("VMWare regs string -->", self.vmware_regs_string)
        print("Xen regs string -->", self.xen_regs_string)

        print("Low number of processors -->", self.num_processors)
        print("Low RAM -->", self.ram_size)

        print("Is running in Docker? -->", self.is_docker)

        print("Parallel MAC -->", self.parallel_mac)
        print("VirtualBox MAC -->", self.virtualbox_mac)
        print("VMWare MAC -->", self.vmware_mac)
        print("Xen MAC -->", self.xen_mac)

        print("Activity has been stopped? -->", self.activity_stopped)

    def check_registry_exists(self, reg_path):
        reg_str = reg_path[0:4]
        try:
            if reg_str == "HKLM":
                reg = winreg.ConnectRegistry(None, winreg.HKEY_LOCAL_MACHINE)
            elif reg_str != "HKCU": 
                reg = winreg.ConnectRegistry(None, winreg.HKEY_CURRENT_USER)
            elif reg_str != "HKCR": 
                reg = winreg.ConnectRegistry(None, winreg.HKEY_CLASSES_ROOT)

            sub_key = reg_path[5:]
            key = winreg.OpenKey(reg, sub_key)
            winreg.CloseKey(reg)
            return True
        except FileNotFoundError as fnfe:
            return False

    def get_all_values(self, key):
        aux_dict = {}
        try:
            i = 0
            while True:
                name, value, type = winreg.EnumValue(key, i)
                aux_dict[str(name)] = str(value)
                i+=1
        except WindowsError:
            return aux_dict

    def check_registry_by_value(self, reg_path, key_name, value):
        reg_str = reg_path[0:4]
        try:
            if reg_str == "HKLM":
                reg = winreg.ConnectRegistry(None, winreg.HKEY_LOCAL_MACHINE)
            elif reg_str != "HKCU": 
                reg = winreg.ConnectRegistry(None, winreg.HKEY_CURRENT_USER)
            elif reg_str != "HKCR": 
                reg = winreg.ConnectRegistry(None, winreg.HKEY_CLASSES_ROOT)

            sub_key = reg_path[5:]
            key = winreg.OpenKey(reg, sub_key)
            aux_dict = self.get_all_values(key)
            count = 0 
            for key in aux_dict:
                if key == key_name:
                    if aux_dict[key].lower() == value.lower():
                        count += 1
            winreg.CloseKey(reg)

            if count > 0: return True
            return False
        except FileNotFoundError as fnfe:
            return False

    def check_mac_address(self, address):
        local_mac = ':'.join((['{:02x}'.format((uuid.getnode() >> ele) & 0xff) for ele in range(0,8*6,8)][::-1]))
        return local_mac[0:8].lower() == address.lower()

    def file_or_dir_detection(self, names_list):
        for fod in names_list:
            if os.path.exists(fod): 
                return True
        return False
    
    def check_registries_exists(self, regs_list):
        for reg in regs_list:
            if self.check_registry_exists(reg):
                return True
        return False

    def check_string_in_registries(self, regs_list):
        for reg in regs_list:
            if self.check_registry_by_value(reg[0], reg[1], reg[2]):
                return True
        return False

    def check_mac_address_bylist(self, mac_list):
        for m in mac_list:
            if self.check_mac_address(m):
                return True
        return False

    def in_docker(self):
        try:
            with open('/proc/1/cgroup', 'rt') as ifh:
                return 'docker' in ifh.read()
        except:
            return False

    def check_num_processors(self):
        try:
            return psutil.cpu_count()
        except:
            return -1

    def get_ram_size(self):
        try:
            bytes = psutil.virtual_memory()
            return bytes.total / 1e9
        except:
            return -1

    def get_screen_res(self):
        try:
            return (win32api.GetSystemMetrics(0), win32api.GetSystemMetrics(1))
        except:
            return -1

    def get_harddrive_size(self, free_space=False):
        try:
            hdd = psutil.disk_usage('/')
            if free_space:
                return hdd.free / 1e9
            return hdd.total / 1e9
        except:
            return -1

    def delay_anti_cuckoo(self, delay):
        try:
            start_time = time.time()
            time.sleep(delay)
            return False
        except:
            if time.time() - start_time < delay:
                return True

    
    
if __name__ == "__main__":
    start_time = time.time()
    ved = VirtualEnvironmentDetector()
    ved.print_check_results()
    print("--- %s seconds ---" % (time.time() - start_time))
    input("ENTER to exit.")
