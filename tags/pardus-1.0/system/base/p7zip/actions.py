#!/usr/bin/python
# -*- coding: utf-8 -*- 
#
# Copyright 2005 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.
#
# Onur Küçük <onur@pardus.org.tr>

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

WorkDir = "p7zip_4.30"

def setup():
    pisitools.dosed("makefile*", "HEDE_getCXXFLAGS", get.CXXFLAGS())
    pisitools.dosed("makefile*", "HEDE_getCXX", get.CXX())
    pisitools.dosed("makefile*", "HEDE_getCC", get.CC())

def build():
    autotools.make("all2")

def install():
    pisitools.doexe("bin/7z", "/usr/lib/p7zip")
    pisitools.doexe("bin/7za", "/usr/lib/p7zip")
    pisitools.doexe("bin/7zCon.sfx", "/usr/lib/p7zip")

    pisitools.doexe("bin/Codecs/*", "/usr/lib/p7zip/Codecs")
    pisitools.doexe("bin/Formats/*", "/usr/lib/p7zip/Formats")

    pisitools.doman("man1/7z.1", "man1/7za.1")
    pisitools.dodoc("ChangeLog", "README", "TODO", "DOCS/*.txt")
    pisitools.dohtml("DOCS/MANUAL/*")

