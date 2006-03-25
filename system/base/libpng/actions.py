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
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

def setup():
    pisitools.dosed("scripts/makefile.linux", "-O3", get.CFLAGS())
    shelltools.move("scripts/makefile.linux", "Makefile")

def build():
    autotools.make("CC=\"%s\" CXX=\"%s\"" % (get.CC(), get.CXX()))

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())
    pisitools.dodoc("ANNOUNCE", "CHANGES", "KNOWNBUG", "README", "TODO", "Y2KINFO")
