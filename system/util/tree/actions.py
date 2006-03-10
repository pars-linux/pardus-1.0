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
from pisi.actionsapi import get

def build():
    autotools.make("CC=\"%s\" CFLAGS=\"%s -DLINUX_BIGFILE\"" % (get.CC(), get.CFLAGS()))

def install():
    pisitools.dobin("tree")
    pisitools.doman("tree.1")
    pisitools.dodoc("CHANGES", "README*")
