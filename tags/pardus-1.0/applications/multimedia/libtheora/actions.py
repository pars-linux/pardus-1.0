#!/usr/bin/python
# -*- coding: utf-8 -*- 
#
# Copyright 2005 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.
#
# S.Çağlar Onur <caglar@uludag.org.tr>

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

WorkDir = "libtheora-1.0alpha5"

def setup():
    pisitools.dosed("Makefile.in", "SUBDIRS = .*", "SUBDIRS = lib include doc")

    autotools.configure("--enable-shared")

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s \
                         docdir=/usr/share/doc/%s" % (get.installDIR(), get.srcTAG()))

    pisitools.dodoc("README")
