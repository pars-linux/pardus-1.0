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
    autotools.configure("--bindir=/bin --disable-nls")

    pisitools.dosed("Makefile", "-lgcrypt", "/usr/lib/libgcrypt.a")
    pisitools.dosed("src/Makefile", "-lgcrypt", "/usr/lib/libgcrypt.a")
    pisitools.dosed("Makefile", "-lgpg-error", "/usr/lib/libgpg-error.a")
    pisitools.dosed("src/Makefile", "-lgpg-error", "/usr/lib/libgpg-error.a")
 
    pisitools.dosed("src/Makefile", "-lpopt", "/usr/lib/libpopt.a")


def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=\"%s\"" % get.installDIR())

