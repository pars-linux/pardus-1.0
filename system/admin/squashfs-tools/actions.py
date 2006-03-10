#!/usr/bin/python
# -*- coding: utf-8 -*- 
#
# Copyright 2005 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.
#
# Onur Küçük <onur@uludag.org.tr>

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

WorkDir = "squashfs2.2-r2/squashfs-tools"

def setup():
    pisitools.dosed("Makefile", "-O2", "${CFLAGS}")

def build():
    autotools.make("CC=\"%s\"" % get.CC())

def install():
    pisitools.dobin("mksquashfs")
    shelltools.cd("..")
    pisitools.dodoc("README*", "ACKNOWLEDGEMENTS", "CHANGES", "PERFORMANCE.README")

