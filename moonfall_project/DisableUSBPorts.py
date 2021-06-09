import winreg
import os
import sys

class DisableUSBPorts(object):

    DISABLE_KEY_LOCATION = "Software\\Microsoft\\Windows\\CurrentVersion\\Policies\\System" #TODO change this location

    def __init__(self):
        pass

    def enable_ports(self, port_id=None):
        pass

    def disable_ports(self, port_id=None):
        pass

if __name__ == "__main__":
    pass