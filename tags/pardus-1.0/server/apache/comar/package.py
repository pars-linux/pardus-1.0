#!/usr/bin/python

import os

def postInstall():
    os.system("/usr/bin/chown root:root /usr/sbin/suexec2")
    os.system("/usr/bin/chmod 04710 /usr/sbin/suexec2")
