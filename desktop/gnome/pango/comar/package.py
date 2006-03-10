#!/usr/bin/python

import os

def postInstall():
    f = open("/etc/pango/pango.modules", "w")
    p = os.popen("/usr/bin/pango-querymodules", "r")
    f.writelines(p.readlines())
    f.close()
    p.close()

