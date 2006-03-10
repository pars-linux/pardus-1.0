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
from pisi.actionsapi import libtools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

WorkDir = "cdparanoia-III-alpha9.8"

def setup():
    pisitools.dosym("configure.guess", "config.guess")
    pisitools.dosym("configure.sub", "config.sub")
    libtools.gnuconfig_update()
    pisitools.remove("config.sub")
    pisitools.remove("config.guess")
    
    shelltools.export("CFLAGS", "%s -I%s/interface" % (get.CFLAGS(), get.curDIR()))
    shelltools.export("CXXLAGS", "%s -I%s/interface" % (get.CXXFLAGS(), get.curDIR()))
    autotools.configure()

def build():
    autotools.make("OPT=\"%s\"" % get.CFLAGS())

def install():
    pisitools.dodir("/usr/bin")
    pisitools.dodir("/usr/lib")
    pisitools.dodir("/usr/include")
    pisitools.dodir("/usr/share/man/man1")
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())
    pisitools.dodoc("FAQ.txt", "README")
