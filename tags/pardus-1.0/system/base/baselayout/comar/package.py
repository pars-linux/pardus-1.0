#!/usr/bin/python

import os
import glob
import shutil

def postInstall():
    os.system("/var/lib/pisi/scripts/baselayout.postinstall")

    if not os.path.exists("/root/"):
        shutil.copytree("/etc/skel", "/root")
    else:
        for file in glob.glob("/etc/skel/.*"):
            os.system("/usr/bin/cp -fdr %s /root" % file)
        
    os.chown("/root", 0, 0)
    os.chmod("/root", 0700)
