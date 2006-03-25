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
    pisitools.dosed("Makefile", "^CC =.*", "CC = %s -Wall -I. %s" % (get.CC(), get.CFLAGS()))
    pisitools.dosed("Makefile", "^modes.tab.c", "modes.tab.h modes.tab.c")

def build():
    autotools.make()

def install():
    pisitools.dobin("fbset")
    pisitools.dobin("modeline2fb")
    pisitools.doman("fb.modes.5", "fbset.8")
    pisitools.dodoc("etc/fb.modes.*", "INSTALL")


