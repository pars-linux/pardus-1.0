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
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

def setup():
    shelltools.export("CPPFLAGS", "%s -I/usr/include/libmpeg3" % get.CXXFLAGS())

    autotools.configure("--enable-fbdev \
                         --enable-mmx \
                         --enable-sse \
                         --enable-libmpeg3 \
                         --enable-jpeg \
                         --enable-png \
                         --enable-gif \
                         --enable-freetype \
                         --enable-sysfs \
                         --disable-sdl \
                         --disable-multi \
                         --disable-debug \
                         --disable-static \
                         --with-gfxdrivers=\"all\"")
                        
def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())
    pisitools.dodoc("AUTHORS", "ChangeLog", "NEWS", "README*", "TODO")
    pisitools.dohtml("docs/html/")
