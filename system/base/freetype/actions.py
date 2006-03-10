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
    shelltools.export("CFLAGS", "-fno-strict-aliasing")
    shelltools.export("CXXFLAGS", "-fno-strict-aliasing")
    autotools.configure()

def build():
    autotools.make("setup CFG=\"--host=%s --prefix=/usr --with-zlib --libdir=/usr/lib\" unix" % get.HOST())

def install():
    autotools.rawInstall("DESTDIR=\"%s\"" % get.installDIR())

    pisitools.dodoc("ChangeLog", "README", "docs/CHANGES", "docs/CUSTOMIZE", "docs/DEBUG", "docs/*.txt", "docs/PATENTS", "docs/TODO")
