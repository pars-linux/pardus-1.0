#!/usr/bin/python
# -*- coding: utf-8 -*- 
#
# Copyright 2005 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.
#
# Bahadır Kandemir <bahadir@pardus.org.tr>

from pisi.actionsapi import autotools
from pisi.actionsapi import libtools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

WorkDir = "w3c-libwww-5.4.0"

def setup():
    shelltools.export("WANT_AUTOCONF", "2.50")

    libtools.libtoolize("-c -f")

    autotools.aclocal()
    autotools.autoconf()

    autotools.configure("--without-mysql \
                         --enable-shared \
                         --enable-static \
                         --with-zlib \
                         --with-md5 \
                         --with-expat \
                         --with-ssl")

def build():
    autotools.make("check-am")
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=\"%s\"" % get.installDIR())
    
    pisitools.dodoc("ChangeLog")
    pisitools.dohtml(".")
