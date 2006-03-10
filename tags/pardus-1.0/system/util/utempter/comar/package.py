#!/usr/bin/python

import os

def postInstall():

    ugstr = "root:utmp"

    os.spawnvp(os.P_NOWAIT, "/usr/bin/chown", ["/usr/bin/chown", ugstr, "/usr/sbin/utempter"])
    os.spawnvp(os.P_NOWAIT, "/usr/bin/chmod", ["/usr/bin/chmod", "2775", "/usr/sbin/utempter"])

    for file in ["/var/log/wtmp", "/var/run/utmp"]:
        if os.path.exists(file):
            os.spawnvp(os.P_NOWAIT, "/usr/bin/chown", ["/usr/bin/chown", ugstr, file])
            os.spawnvp(os.P_NOWAIT, "/usr/bin/chmod", ["/usr/bin/chmod", "664", file])
            
