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

WorkDir = "ungrab-winmodem"

def setup():
    pisitools.dosed("Makefile", "SUBDIRS=\$(shell pwd)", "SUBDIRS=%s" % get.srcDIR())
    pisitools.dosed("Makefile", "SUBDIRS=", "M=")

def build():
    autotools.make("KERNEL_DIR=/usr/src/linux")

def install():
    pisitools.insinto("/lib/modules/%s/misc" % get.curKERNEL(), "*.ko")
    pisitools.dodoc("Readme.txt")

