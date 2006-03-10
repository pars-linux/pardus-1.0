#/usr/bin/python

import os

def postInstall():
    # Recalculate disk geometry and generate preload file
    os.system("/usr/sbin/prepare_preload_file -c < /etc/preload.d/OpenOffice.preload_phase2 > /etc/preload.d/OpenOffice.preload")
