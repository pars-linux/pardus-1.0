#!/usr/bin/python

import os

def postInstall():
    if os.path.exists(/usr/bin/fc-cache):
        os.system('HOME="/root" /usr/bin/fc-cache -f')
