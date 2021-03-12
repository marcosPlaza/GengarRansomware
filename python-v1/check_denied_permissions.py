#!/usr/bin/python

import os
import sys
import win32api

# Assuming /tmp/foo.txt exists and has read/write permissions.


def checking_access(filename):
    access = dict()

    access['R'] = os.access(filename, os.R_OK)
    access['W'] = os.access(filename, os.W_OK)

    return {filename:access}


if __name__ == '__main__':
    local_drives = win32api.GetLogicalDriveStrings()  # Cheking drives connected
    local_drives = local_drives.split('\000')[:-1]

    for d in local_drives:
        for root, dirs, files in os.walk(d):
            for fn in files:
                full_path = root + os.sep + fn
                check_dict = checking_access(full_path)
                if not check_dict[full_path]['R'] or not check_dict[full_path]['W']:
                    print(check_dict)