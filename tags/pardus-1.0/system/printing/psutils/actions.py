#!/usr/bin/python
# -*- coding: utf-8 -*- 
#
# Copyright 2005 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.
#
# S.Çağlar Onur <caglar@uludag.org.tr>

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

WorkDir = "psutils"

def setup():
    pisitools.dosed("Makefile.unix", "/usr/local", "$(DESTDIR)/usr")
    pisitools.dosed("Makefile.unix", "-DUNIX -O", "-DUNIX %s" % get.CFLAGS())
    shelltools.move("Makefile.unix", "Makefile")

def build():
    autotools.make()

def install():
    pisitools.dodir("/usr/bin")
    pisitools.dodir("/usr/share/man")

    autotools.rawInstall("DESTDIR=%s" % get.installDIR())
