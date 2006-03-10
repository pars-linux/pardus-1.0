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
from pisi.actionsapi import libtools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

def setup():
    shelltools.export("WANT_AUTOMAKE", "1.8")
    shelltools.export("WANT_AUTOCONF", "2.5")

    libtools.libtoolize("--force --copy --automake")
    autotools.autoheader()
    autotools.aclocal()
    autotools.automake("-a -f -c")
    autotools.autoconf()

    autotools.configure("--enable-shared --disable-djbfft")

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=\"%s\" docdir=/usr/share/doc/%s/html" % (get.installDIR(), get.srcTAG()))
    pisitools.dodoc("AUTHORS", "ChangeLog", "HISTORY", "NEWS", "README", "TODO", "doc/liba52.txt")
