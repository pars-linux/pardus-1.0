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

WorkDir = "wireless_tools.28"

def setup():
    pisitools.dosed("Makefile", "^CFLAGS=", "CFLAGS=%s " % get.CFLAGS())

#    sed -i "s:\(@\$(LDCONFIG).*\):#\1:" ${S}/Makefile

    pisitools.dosed("Makefile", "^\(INSTALL_MAN= \$(PREFIX)\)/man/", "\1/share/man")

def build():
    autotools.make("WARN=\"\"")

def install():
    autotools.rawInstall("PREFIX=%s/usr" % get.installDIR())
    pisitools.dodoc("CHANGELOG.h", "COPYING", "INSTALL", "HOTPLUG.txt", "PCMCIA.txt", "README")
