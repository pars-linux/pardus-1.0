#!/usr/bin/python
# -*- coding: utf-8 -*- 
#
# Copyright 2005 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.
#
# S.Çağlar Onur <caglar@uludag.org.tr>

from pisi.actionsapi import kde
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

def setup():
    shelltools.export("LDFLAGS", "%s -Wl,-z,now" % get.LDFLAGS())
    
    kde.configure("--disable-dependency-tracking \
                   --enable-maintainer-mode \
                   --disable-pinentry-gtk \
                   --disable-pinentry-gtk2 \
                   --enable-pinentry-qt \
                   --disable-pinentry-curses \
                   --disable-fallback-curses")

def build():
    kde.make()

def install():
    kde.install()
    shelltools.chmod("%s/usr/kde/3.5/bin/pinentry" % get.installDIR(), 04755)
