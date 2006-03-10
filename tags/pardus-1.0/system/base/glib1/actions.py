#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright © 2005  TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.
#
# S.Çağlar Onur <caglar@uludag.org.tr>

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

WorkDir = "glib-1.2.10"

def setup():
    autotools.configure("--with-threads=posix --enable-debug=yes")

def build():
    autotools.make()

def install():
    autotools.install()
    pisitools.dodoc("AUTHORS", "ChangeLog", "README*", "INSTALL", "NEWS")
    pisitools.dohtml("docs")

    shelltools.chmod("%s/usr/lib/libgmodule-1.2.so.*" % get.installDIR())
