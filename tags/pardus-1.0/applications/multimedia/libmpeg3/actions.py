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

def setup():
    # libmpeg2 comes with a52 but its quiet old, so we link against the system...
    shelltools.unlink("Makefile.a52")
    shelltools.touch("Makefile.a52")

    shelltools.unlinkDir("a52dec-0.7.3/")
    shelltools.makedirs("a52dec-0.7.3")

    shelltools.sym("/usr/include/a52dec", "a52dec-0.7.3/include")

    pisitools.dosed("Makefile", "LIBS = -lm -lpthread", "LIBS = -lm -lpthread -L/usr/lib -la52")

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=\"%s/usr\"" % get.installDIR())
    pisitools.dohtml("docs")
