#!/usr/bin/python
# -*- coding: utf-8 -*- 
#
# Copyright 2005 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.
#
# Onur Küçük <onur@uludag.org.tr>

from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

def install():
    for lib in shelltools.ls("*.so"):
        pisitools.dolib_so(lib)
        pisitools.dosym("/usr/lib/%s" % lib, "/usr/lib/%s.0" % lib)

    for header in shelltools.ls("*.h"):
        pisitools.insinto("/usr/include", header)
    
    pisitools.dohtml("DivX MPEG-4 Codec and Its Interface.htm")
