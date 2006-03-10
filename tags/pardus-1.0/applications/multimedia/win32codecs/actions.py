#!/usr/bin/python
# -*- coding: utf-8 -*- 
#
# Copyright 2005 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.
#
# Onur Küçük <onur@uludag.org.tr>

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

WorkDir = "all-20050412"

def setup():
    pass

def build():
    pass

def install():
    pisitools.dodir("/usr/lib/win32")
    pisitools.insinto("/usr/lib/win32", "*")
    shelltools.chmod("%s/usr/lib/win32/*" % get.installDIR(), mode = 0644)
    
    # Real audio / video
    pisitools.dodir("/usr/lib/real")
    pisitools.domove("/usr/lib/win32/*.so.6.0", "/usr/lib/real/")
    for file in shelltools.ls("%s/usr/lib/real/*.so.6.0" % get.installDIR()):
        pisitools.dosym(file.replace(get.installDIR(), ""), "/usr/lib/win32/%s" % shelltools.baseName(file))

    pisitools.dodoc("README")
