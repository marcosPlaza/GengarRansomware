import winreg

"""
Check here - https://resources.infosecinstitute.com/topic/malware-anti-analysis-techniques-ways-bypass/
https://www.goggleheadedhacker.com/blog/post/23
Techniques
Check registry entry
Check if registry exists
Check if some file exists
"""
class VirtualEnvironmentDetector:
    # General
    LOCATION_1 = "SYSTEM\\ControlSet001\\Control\\Class\\{4d36e965-e325-11ce-bfc1-08002be10318}\\0000\\DriverDesc"  # If registry exists
    LOCATION_2 = "SYSTEM\\ControlSet001\\Control\\Class\\{4d36e965-e325-11ce-bfc1-08002be10318}\\0000\\ProviderName"  # If registry exists
    LOCATION_3 = "HARDWARE\\DEVICEMAP\\Scsi\\Scsi Port 0\\Scsi Bus 0\\Target Id 0\\Logical Unit Id 0\\Identifier" # Find QEMU or VBOX or VMWare
    LOCATION_4 = "HARDWARE\\Description\\System\\SystemBiosVersion" # Find QEMU or VBOX
    LOCATION_5 = "HARDWARE\\Description\\System\\VideoBiosVersion" # Find VIRTUALBOX
    LOCATION_6 = "SOFTWARE\\Oracle\\VirtualBox Guest Additions" # If registry exists
    LOCATION_7 = "WINDOWS\\system32\\drivers\\VBoxMouse.sys" # Check if file driver exists
    LOCATION_8 = "SOFTWARE\\VMware, Inc.\\VMware Tools" # If registry exists
    LOCATION_9 = "WINDOWS\\system32\\drivers\\vmhgfs.sys" # Check if file driver exists
    LOCATION_10 = "WINDOWS\\system32\\drivers\\vmmouse.sys" # Check if file driver exists
    LOCATION_11 = "WINDOWS\\system32\\drivers\\VBoxControl.exe" # Check if file driver exists

    def __init__(self):
        pass

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

    def check_driver_exists(self, driver_path):
        pass

    # IDT address
    
if __name__ == "__main__":

    input("Press key to continue")