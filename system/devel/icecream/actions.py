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

WorkDir ="icecream"

def setup():
    pisitools.dosed("configure.in", "CFLAGS=-g", "CFLAGS=%s" % get.CFLAGS())
    pisitools.dosed("configure.in", "CXXFLAGS=-g", "CXXFLAGS=%s" % get.CXXFLAGS())
    
    autotools.rawConfigure("--prefix=/opt/icecream")

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())
