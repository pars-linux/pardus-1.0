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
from pisi.actionsapi import libtools
from pisi.actionsapi import get

def setup():
    shelltools.export("WANT_AUTOMAKE", "1.6")
    shelltools.export("WANT_AUTOCONF", "2.5")

    libtools.libtoolize("--force --copy")
    autotools.aclocal()
    autotools.automake()
    autotools.autoconf()

    shelltools.export("CPPFLAGS", "%s -Wno-deprecated" % get.CFLAGS())
    
    autotools.configure()

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    pisitools.dosym("libid3-3.8.so.3", "/usr/lib/libid3-3.8.so.0.0.0")
    pisitools.dosym("libid3-3.8.so.0.0.0", "/usr/lib/libid3-3.8.so.0")

    pisitools.dodoc("AUTHORS", "ChangeLog", "HISTORY", "INSTALL", "README", "THANKS", "TODO")
