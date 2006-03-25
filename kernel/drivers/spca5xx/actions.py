#!/usr/bin/python
# -*- coding: utf-8 -*- 
#
# Copyright 2005 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.
#
# Onur Küçük <onur@pardus.org.tr>

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

def setup():
    pisitools.dosed("Makefile", "SUBDIRS=", "M=")

def build():
    autotools.make("KERNELDIR=/usr/src/linux default")

def install():
    pisitools.insinto("/lib/modules/%s/extra" % get.curKERNEL(), "*.ko")
    pisitools.dodoc("CHANGELOG", "INSTALL", "README*")

