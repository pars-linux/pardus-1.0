#!/usr/bin/python
# -*- coding: utf-8 -*- 
#
# Copyright 2005 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.
#
# Onur Küçük <onur@pardus.org.tr>

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

WorkDir="avifile-0.7-0.7.43"

def setup():
    # make sure pkgconfig file is correct
    shelltools.unlink("avifile.pc")

    # Fix qt detection
    pisitools.dosed("configure", "extern \"C\" void exit(int);", "/* extern \"C\" void exit(int); */")

    # adding CFLAGS by default which exists only for x86 is no good idea
    # but I can't get it through gcc 3.4.3 without omit-frame-pointer
    pisitools.dosed("ffmpeg/libavcodec/libpostproc/Makefile.in", "^AM_CFLAGS = .*", "AM_CFLAGS = -fomit-frame-pointer")
    pisitools.dosed("plugins/libwin32/loader/Makefile.in", "^AM_CFLAGS = .*", "AM_CFLAGS = -fomit-frame-pointer")

    # Make sure we include freetype2 headers before freetype1 headers, else Xft2 borks
    shelltools.export("C_INCLUDE_PATH", "%s:/usr/include/freetype2" % get.ENV("C_INCLUDE_PATH"))
    shelltools.export("CPLUS_INCLUDE_PATH", "%s:/usr/include/freetype2" % get.ENV("CPLUS_INCLUDE_PATH"))

    # filter-flags "-momit-leaf-frame-pointer"
    
    shelltools.system("rm acinclude.m4")
    shelltools.system("ACLOCAL_FLAGS=\"-I m4\" ./autogen.sh --copy --force")
    shelltools.export("FFMPEG_CFLAGS", "%s" % get.CFLAGS())
    autotools.configure("--disable-static \
                         --enable-freetype2 \
                         --enable-xv \
                         --enable-sdl \
                         --enable-sdltest \
                         --enable-a52 \
                         --enable-ffmpeg-a52 \
                         --enable-libz \
                         --enable-vorbis \
                         --enable-oggtest \
                         --enable-vorbistest \
                         --with-x \
                         --enable-xft \
                         --enable-samples \
                         --disable-vidix \
                         --with-fpic \
                         --enable-lame-bin \
                         --enable-oss \
                         --disable-xvid \
                         --enable-xvid4 \
                         --enable-quiet \
                         --enable-x86opt \
                         --with-qt-prefix=%s" % get.qtDIR())

def build():
    autotools.make()

def install():
    pisitools.dodir("/usr/lib/win32")
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())
    pisitools.dodoc("README", "INSTALL")
    pisitools.dodoc("doc/CREDITS", "doc/EXCEPTIONS", "doc/TODO", "doc/VIDEO-PERFORMANCE", "doc/WARNINGS", "doc/KNOWN_BUGS")

