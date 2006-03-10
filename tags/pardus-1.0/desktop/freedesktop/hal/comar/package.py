#!/usr/bin/python

import os

def postInstall():
    try:
        os.makedirs("/var/run/hald")
    except OSError:
        pass
    os.spawnvp(os.P_NOWAIT, "/usr/bin/chown", ["/usr/bin/chown", "haldaemon:haldaemon", "/var/run/hald"])
    os.system("/sbin/rc-update add hald default")
    os.system("/sbin/depscan.sh")
