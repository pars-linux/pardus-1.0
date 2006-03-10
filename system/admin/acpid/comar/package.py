#!/usr/bin/python

import os

def postInstall():
    os.system("/sbin/rc-update add acpid boot")
    os.system("/sbin/depscan.sh")
