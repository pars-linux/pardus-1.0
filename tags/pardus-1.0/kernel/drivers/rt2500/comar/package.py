#!/usr/bin/python

import os

def postInstall():
    f = open("/etc/modprobe.conf", "a")
    f.write("\nalias ra0 rt2500")
    f.close()

    os.system("/sbin/modules-update")
