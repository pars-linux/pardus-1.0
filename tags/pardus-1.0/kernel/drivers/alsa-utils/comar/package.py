#!/usr/bin/python

import os

def postInstall():
    os.system("/sbin/rc-update add alsasound boot")
    os.system("/sbin/depscan.sh")
