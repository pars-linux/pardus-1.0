#!/usr/bin/python

import os
import shutil

def postInstall():
    os.system("/var/lib/pisi/scripts/xorg.postinstall")
    os.system("/usr/libexec/opengl-update xorg-x11")
    os.system("/sbin/rc-update add xdm default")
    os.system("/sbin/depscan.sh")
