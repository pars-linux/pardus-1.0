#!/usr/bin/python

import os

def postInstall():
    os.system("/usr/bin/chown root:utmp /usr/bin/screen")
    os.system("/usr/bin/chmod 02755 /usr/bin/screen")
    os.system("/usr/bin/chown root:utmp /var/run/screen")
    os.system("/usr/bin/chmod 0755 /var/run/screen")

    # suid
    os.system("/usr/bin/chmod u+s /usr/bin/screen")
    os.system("/usr/bin/chmod go-w /var/run/screen")
