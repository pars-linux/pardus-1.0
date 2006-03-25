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
from pisi.actionsapi import get

def setup():
    autotools.configure("--disable-static \
                        --sysconfdir=/etc/aspell \
                        --enable-docdir=/usr/share/doc/%s" % get.srcTAG())

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())
    
    pisitools.dodoc("README*", "TODO")

    pisitools.domove("/usr/share/doc/%s/man-html" % get.srcTAG(), "/usr/share/doc/%s/html" % get.srcTAG())
    pisitools.domove("/usr/share/doc/%s/man-text" % get.srcTAG(), "/usr/share/doc/%s/text" % get.srcTAG())

    # install ispell/aspell compatibility scripts
    pisitools.doexe("scripts/ispell", "/usr/bin")
    pisitools.domove("/usr/bin/ispell", "/usr/bin/", "ispell-aspell")
    pisitools.doexe("scripts/spell", "/usr/bin")
    pisitools.domove("/usr/bin/spell", "/usr/bin/", "spell-aspell")
