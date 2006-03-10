#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright © 2005  TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.
#
# S.Çağlar Onur <caglar@uludag.org.tr>

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

def setup():
    pisitools.dosed("Makefile", "^ALL_CFLAGS += $(call check_gcc,-fweb,)")

def build():
    autotools.make("lib64=/lib CC=%s CPPFLAGS=\"%s\" CFLAGS=\"%s\" LDFLAGS=\"%s\"" % \
                   (get.CC(), get.CXXFLAGS(), get.CFLAGS(), get.LDFLAGS()))
                   
def install():
    autotools.rawInstall("ldconfig=\"true\" DESTDIR=%s" % get.installDIR())
    pisitools.dodoc("sysctl.conf", "BUGS", "NEWS", "TODO", "ps/HACKING")

    pisitools.dodir("/usr/include/proc/")
    shelltools.move("proc/*.h", "%s/usr/include/proc/" % get.installDIR())
