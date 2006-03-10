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
    pisitools.dosed("make/linux/Makefile", "CXXFLAGS=", "CXXFLAGS+=")
    shelltools.export("CFLAGS", "%s -fPIC" % get.CFLAGS())
    shelltools.export("CXXFLAGS", "%s -fPIC" % get.CXXFLAGS())

def build():
    shelltools.cd("make/linux")
    autotools.make("PREFIX=/usr")

def install():
    shelltools.cd("make/linux")
    autotools.install("libdir=%s/usr/lib" % get.installDIR())
    pisitools.dodoc("../../LICENSE.*")
