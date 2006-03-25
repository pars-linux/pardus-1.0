#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright © 2005  TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.
#
# S.Çağlar Onur <caglar@pardus.org.tr>

from pisi.actionsapi import autotools
from pisi.actionsapi import shelltools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

def setup():
    shelltools.export("CFLAGS", " %s -Wl,-z,now" % get.CFLAGS())
    shelltools.export("CXXFLAGS", "%s -Wl,-z,now" % get.CXXFLAGS())

    autotools.configure()

def build():
    autotools.make()

def install():
    #this is where we mount stuff
    pisitools.dodir("/media")

    pisitools.doexe("src/pmount", "/usr/bin")
    pisitools.doexe("src/pumount", "/usr/bin")
    pisitools.doexe("src/pmount-hal", "/usr/bin")

    pisitools.dodoc("AUTHORS", "CHANGES", "TODO")
    pisitools.doman("man/pmount.1", "man/pumount.1", "man/pmount-hal.1")
