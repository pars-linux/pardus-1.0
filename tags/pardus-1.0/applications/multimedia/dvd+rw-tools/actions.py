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
    pisitools.dosed("Makefile.m4", "^CFLAGS=\$(WARN).*", "CFLAGS=" + get.CFLAGS())
    pisitools.dosed("Makefile.m4", "^CXXFLAGS=\$(WARN).*", "CXXFLAGS=" + get.CXXFLAGS() + " -fno-exceptions")

def build():
    autotools.make()

def install():
    pisitools.dobin("dvd+rw-booktype")
    pisitools.dobin("dvd+rw-format")
    pisitools.dobin("dvd+rw-mediainfo")
    pisitools.dobin("growisofs")
    
    pisitools.dohtml(".")
    pisitools.doman("growisofs.1")
