#!/usr/bin/python
# -*- coding: utf-8 -*-

WorkDir="."

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools

def build():
    autotools.compile("-o rpmoffset rpmoffset.c")
    
def install():
    pisitools.insinto("/usr/bin/", "rpmoffset")
    pisitools.doexe("rpm2targz", "/usr/bin/")
    pisitools.dodoc("rpm2targz.README")
