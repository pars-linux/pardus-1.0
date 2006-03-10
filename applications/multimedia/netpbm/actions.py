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
from pisi.actionsapi import get

def setup():
    pisitools.dosed("lib/Makefile", "$(CFLAGS)", "$(CFLAGS) -fPIC")
    pisitools.dosed("lib/Makefile", "$(LDFLAGS)", "$(LDFLAGS) -fPIC")
    pisitools.dosed("lib/util/Makefile", "$(CCOPT)", "$(CCOPT) -fPIC")

def build():
    autotools.make("-j1 CC=\"%s\" CXX=\"%s\"" % (get.CC(), get.CXX()))

def install():
    pisitools.dodir("/")
    autotools.make("package pkgdir=%s/usr/" % get.installDIR())
    pisitools.dodoc("%s/usr/misc/*" % get.installDIR())

    pisitools.remove("/usr/VERSION")
    pisitools.remove("/usr/pkginfo")
    pisitools.remove("/usr/README")
    pisitools.remove("/usr/bin/doc.url")
    pisitools.removeDir("/usr/misc")
    pisitools.removeDir("/usr/man/web")

    pisitools.domove("/usr/link/libnetpbm.a", "/usr/lib")
    pisitools.domove("/usr/man", "/usr/share")
    pisitools.removeDir("usr/link")

    pisitools.dodoc("README", "doc/*")
