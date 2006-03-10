#/usr/bin/python

import os

def postInstall():
    os.system("/usr/bin/fc-cache -v")
