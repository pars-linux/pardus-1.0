#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright © 2005  TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.
#
# S.Çağlar Onur <caglar@uludag.org.tr>

from pisi.actionsapi import autotools
from pisi.actionsapi import get
from pisi.actionsapi import pisitools

def setup():
    pisitools.dosed("unix/Makefile", "-O2", get.CFLAGS())

def build():
    autotools.make("-f unix/Makefile CC=%s CPP=%s generic" % (get.CC(), get.CXX()))

def install():
    pisitools.dobin("zip")
    pisitools.dobin("zipcloak")
    pisitools.dobin("zipnote")
    pisitools.dobin("zipsplit")
    
    pisitools.doman("man/*.1")
    pisitools.dodoc("BUGS", "CHANGES", "MANUAL", "README", "TODO", "WHATSNEW", "WHERE")
