#!/usr/bin/python

import os

def postInstall():
    os.spawnvp(os.P_NOWAIT, "/usr/bin/chown", ["/usr/bin/chown", "root:users", "/var/lib/lock/sane"])
    os.spawnvp(os.P_NOWAIT, "/usr/bin/chmod", ["/usr/bin/chmod", "g+w", "/var/lib/lock/sane"])
