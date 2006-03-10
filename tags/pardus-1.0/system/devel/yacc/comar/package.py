#!/usr/bin/python

import os

def postInstall():
    if not os.path.exists("/usr/bin/yacc") and os.path.exists("/usr/bin/bison"):
        os.symlink("bison", "/usr/bin/yacc")
