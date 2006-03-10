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
from pisi.actionsapi import libtools
from pisi.actionsapi import get

def setup():
    autotools.configure("--with-x \
                        --disable-xfree-ext \
                        --with-quicktime \
                        --with-v4l \
                        --without-gtk \
                        --with-sdl \
                        --with-dv=/usr \
                        --enable-largefile \
                        --with-dv-yv12 \
                        --enable-simd-accel \
                        --with-jpeg-mmx=/usr/include/jpeg-mmx \
                        --enable-cmov-extension")

def build():
    # seems mjpegtools does not play nicely with sse2
    shelltools.export("CFLAGS", "%s -mno-sse2" % get.CFLAGS())
    autotools.make("CFLAGS=\"%s\" -j1" % get.CFLAGS())

def install():
    autotools.install()
    pisitools.dodoc("mjpeg_howto.txt", "README", \
                    "PLANS", "NEWS", "README.AltiVec", \
                    "README.avilib", "README.DV", "README.glav", \
                    "README.lavpipe", "README.transist", "TODO", \
                    "HINTS", "BUGS", "ChangeLog", "AUTHORS", "CHANGES")
