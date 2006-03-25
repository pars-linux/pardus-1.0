#!/usr/bin/python
# -*- coding: utf-8 -*- 
#
# Copyright 2005 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.
#
# A. Murat Eren <meren@pardus.org.tr>

from pisi.actionsapi import libtools
from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

def setup():
    shelltools.export("WANT_AUTOCONF", "2.5")
    shelltools.export("WANT_AUTOMAKE", "1.7")

    autotools.aclocal("-I m4")
    autotools.autoheader()
    autotools.automake("-afc")
    autotools.autoconf()

    libtools.libtoolize("--copy --force")

    flags = "-mcpu=i686 \
             -O2 \
             -pipe \
             -frename-registers \
             -fomit-frame-pointer \
             -mno-sse \
             -ffunction-sections"

    shelltools.export("CFLAGS", "%s %s" % (get.CFLAGS(), flags))
    shelltools.export("CXXFLAGS", "%s %s" % (get.CXXFLAGS(), flags))

    autotools.configure("--enable-nls \
                         --disable-gnome \
                         --disable-altivec \
                         --disable-speex \
                         --enable-ipv6 \
                         --enable-samba \
                         --enable-mng \
                         --enable-png \
                         --enable-faad \
                         --enable-flac \
                         --with-ogg \
                         --with-vorbis \
                         --with-x \
                         --enable-xinerama \
                         --disable-vidix \
                         --disable-dxr3 \
                         --enable-directfb \
                         --enable-fb \
                         --enable-opengl \
                         --enable-aalib \
                         --enable-caca \
                         --enable-sdl \
                         --enable-libmad --with-external-libmad \
                         --disable-oss \
                         --disable-vcd \
                         --enable-alsa \
                         --enable-arts \
                         --disable-esd \
                         --with-ffmpeg \
                         --with-xv-path=/usr/lib \
                         --disable-optimizations \
                         --disable-optimizations \
                         --disable-dependency-tracking")

def build():
    autotools.make("-j1")

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    pisitools.dodoc("AUTHORS", "ChangeLog", "README", "TODO", "doc/README*", "doc/faq/faq.txt")
    pisitools.dohtml("doc/faq/faq.html", "doc/hackersguide/*.html", "doc/hackersguide/*.png")

    pisitools.removeDir("/usr/share/doc/xine")

