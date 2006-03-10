#!/usr/bin/python

import os

def postInstall():
    if os.path.exists("/usr/bin/hostname") and not os.path.islink("/usr/bin/hostname"):
        os.remove("/usr/bin/hostname")       
