#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2005 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.
#
# S.Çağlar Onur <caglar@pardus.org.tr>

from pisi.actionsapi import pisitools
from pisi.actionsapi import autotools

WorkDir = "unrar"

def build():
    autotools.make("-f makefile.unix CXXFLAGS=\"$CXXFLAGS\"")

def install():
    pisitools.insinto("/usr/bin", "unrar")
    pisitools.dodoc("readme.txt")
            
