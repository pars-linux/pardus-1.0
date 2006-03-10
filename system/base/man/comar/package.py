#!/usr/bin/python

import os
import pwd

def postInstall():
    rootuid = pwd.getpwnam("root")[2]
    rootgid = pwd.getpwnam("root")[3]
    mangid = pwd.getpwnam("man")[3]

    for root, dirs, files in os.walk("/var/cache/man"):
        for f in files:
            fpath = os.path.join(root, f)
            os.chown(fpath, rootuid, mangid)
            os.chmod(fpath, 0664)
        for d in dirs:
            fpath = os.path.join(root, d)
            os.chown(fpath, rootuid, mangid)
            os.chmod(fpath, 0664)

    if os.path.exists("/var/cache/man/whatis"):
        os.chown("/var/cache/man/whatis", rootuid, rootgid)

