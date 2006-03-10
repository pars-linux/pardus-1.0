#/usr/bin/python

import os

def postInstall():
    if os.path.islink("/usr/lib/blender/plugins/include"):
        os.system("/usr/bin/rm -f /usr/lib/blender/plugins/include")
