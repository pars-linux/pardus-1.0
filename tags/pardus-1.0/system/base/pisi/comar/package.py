#/usr/bin/python

import os

def postInstall():
    if not os.path.exists("/var/lib/pisi/package"):
        os.system("mkdir /var/lib/pisi/package")
        os.system("mv /var/lib/pisi/* /var/lib/pisi/package/")
        os.system("mv /var/lib/pisi/package/scripts /var/lib/pisi/")
