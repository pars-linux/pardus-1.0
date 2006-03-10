#/usr/bin/python

import os

def postInstall():
    if not os.path.exists("/home/samba"):
        os.system("/usr/bin/mkdir /home/samba")
        os.system("/usr/bin/chmod 777 /home/samba")
