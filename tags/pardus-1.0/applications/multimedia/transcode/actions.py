#!/usr/bin/python
# -*- coding: utf-8 -*- 
#
# Copyright 2005 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.
#
# S.Çağlar Onur <caglar@pardus.org.tr>

from pisi.actionsapi import shelltools
from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import libtools
from pisi.actionsapi import get

def setup():
    libtools.libtoolize("--copy --force")
    autotools.autoreconf("-i")

    shelltools.export("CFLAGS", "%s -DDCT_YUV_PRECISION=1" % get.CFLAGS())
    shelltools.export("CXXFLAGS", "%s -DDCT_YUV_PRECISION=1" % get.CXXFLAGS())

    autotools.configure("--with-default-xvid=xvid4 \
                        --with-libpostproc-builddir=/usr/lib \
                        --with-mod-path=/usr/lib/transcode \
                        --enable-x \
                        --enable-a52 \
                        --enable-altivec \
                        --enable-avifile \
                        --enable-libdv \
                        --enable-libdvdread \
                        --enable-lame \
                        --enable-libfame \
                        --enable-freetype \
                        --disable-gtk \
                        --enable-imagemagick \
                        --enable-libjpeg \
                        --enable-lzo \
                        --enable-mjpegtools \
                        --enable-mmx \
                        --enable-libmpeg3 \
                        --enable-netstream \
                        --enable-ogg \
                        --enable-vorbis \
                        --enable-libquicktime \
                        --enable-sdl \
                        --enable-sse \
                        --enable-sse2 \
                        --enable-theora \
                        --enable-v4l \
                        --enable-libxml2")
                        
def build():
    autotools.make("-j1 all")

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())
    pisitools.dodoc("AUTHORS", "ChangeLog", "README", "TODO")
