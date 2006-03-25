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
    autotools.configure("--disable-dependency-tracking \
                        --with-jpeg \
                        --with-tiff \
                        --with-zlib \
                        --with-python")
                        
def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s \
                          BINDIR=%s/usr/bin \
                          includedir=\"/usr/include/lcms\"" % (get.installDIR(), get.installDIR()))

    pisitools.insinto("/usr/share/lcms/profiles", "testbed/*.icm")

    pisitools.dodoc("AUTHORS", "README*", "INSTALL", "NEWS", "doc/*")
