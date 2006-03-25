#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright © 2005  TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.
#
# S.Çağlar Onur <caglar@pardus.org.tr>

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

def setup():
    pisitools.dosed("Makefile.def", "options= ", "options= %s " % get.CFLAGS())
    pisitools.dosed("Makefile.def", "CC=cc", "CC=%s" % get.CC())
    shelltools.move("Makefile.def", "Makefile")

def build():
    autotools.make()

def install():
    pisitools.dobin("compress")
    pisitools.dosym("compress", "/usr/bin/uncompress")
    pisitools.doman("compress.1")
