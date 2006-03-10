#!/usr/bin/python

import os

def postInstall():
    os.system("/sbin/rc-update add zemberek-server default")
    os.system("/sbin/depscan.sh")
