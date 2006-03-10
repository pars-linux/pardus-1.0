#!/usr/bin/python

import os

def postInstall():
    os.system("/sbin/rc-update add mdnsd default")
    os.system("/sbin/depscan.sh")
