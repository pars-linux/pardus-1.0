#!/usr/bin/python
# -*- coding: utf-8 -*- 
#
# Copyright 2005 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.
#
# S.Çağlar Onur <caglar@pardus.org.tr>

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import libtools
from pisi.actionsapi import get

def setup():
    autotools.aclocal()
    libtools.libtoolize("--copy --force")
    autotools.automake("-a")
    autotools.autoconf()

    autotools.configure("--with-mylibgd \
                         --disable-dependency-tracking \
                         --without-tcl \
                         --without-tk")

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    pisitools.dodoc("AUTHORS", "ChangeLog", "FAQ.txt", "INSTALL*", "MINTERMS.txt" \
                    "NEWS", "README*", "doc/*.pdf", "doc/Dot.ref")

    pisitools.dohtml(".")
