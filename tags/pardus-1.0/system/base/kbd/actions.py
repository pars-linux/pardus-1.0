#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright © 2005  TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.
#
# S.Çağlar Onur <caglar@pardus.org.tr>

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

def setup():
    pisitools.dosed("src/Makefile.in", "-O2", get.CFLAGS())
    pisitools.dosed("src/Makefile.in", "install -s", "install")

    autotools.rawConfigure("--prefix=/usr --mandir=/usr/share/man --datadir=/usr/share")
                    
def build():
    autotools.make("CC=%s" % get.CC())

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    pisitools.domove("/usr/bin/setfont", "/bin")
    pisitools.dosym("/bin/setfont", "/usr/bin/setfont")

    pisitools.dodoc("CHANGES", "CREDITS", "README")

    pisitools.dohtml("doc/*")
