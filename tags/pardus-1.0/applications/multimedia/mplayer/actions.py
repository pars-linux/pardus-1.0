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
from pisi.actionsapi import get

NoStrip = "/"

def setup():
    shelltools.export("LINGUAS", "tr")
    # shelltools.export("CFLAGS", "%s -O3 -frename-registers" % get.CFLAGS())
    autotools.rawConfigure("--prefix=/usr \
                         --confdir=/usr/share/mplayer \
                         --datadir=/usr/share/mplayer \
                         --enable-runtime-cpudetection \
                         --enable-edl \
                         --enable-largefiles \
                         --enable-menu \
                         --enable-real \
                         --enable-network \
                         --enable-ftp \
                         --with-reallibdir=/usr/lib/real \
                         --with-x11incdir=/usr/include \
                         --disable-fribidi \
                         --disable-cdparanoia \
                         --enable-dvdread \
                         --disable-mpdvdkit \
                         --enable-mencoder \
                         --enable-gui \
                         --enable-x11 \
                         --enable-xinerama \
                         --enable-xv \
                         --enable-gui \
                         --enable-png \
                         --enable-inet6 \
                         --enable-joystick \
                         --enable-rtc \
                         --enable-smb \
                         --enable-freetype \
                         --enable-tv-v4l \
                         --enable-tv-v4l2 \
                         --disable-jack \
                         --enable-divx4linux \
                         --enable-gif \
                         --enable-jpeg \
                         --enable-libdts \
                         --enable-liblzo \
                         --enable-internal-matroska \
                         --enable-internal-faad \
                         --enable-vorbis \
                         --enable-theora \
                         --enable-xvid \
                         --disable-3dfx \
                         --disable-tdfxvid \
                         --disable-tdfxfb \
                         --enable-aa \
                         --enable-directfb \
                         --enable-dvb \
                         --enable-fbdev \
                         --disable-ggi \
                         --enable-caca \
                         --disable-mga \
                         --enable-gl \
                         --enable-sdl \
                         --disable-svga \
                         --enable-tga \
                         --enable-alsa \
                         --enable-arts \
                         --disable-esd \
                         --enable-mad \
                         --enable-nas \
                         --disable-ossaudio \
                         --disable-3dnow \
                         --disable-3dnowex \
                         --enable-sse \
                         --enable-mmx \
                         --enable-mmx2 \
                         --disable-3dnow \
                         --disable-debug \
                         --enable-i18n \
                         --disable-altivec \
                         --disable-gcc-checking \
                         --enable-libcdio \
                         --enable-live \
                         --enable-lirc \
                         --with-livelibdir=/usr/lib/live")

    pisitools.dosed("config.mak", "GIF_LIB =", "GIF_LIB = -lungif")

def build():
    autotools.make()

    # Build shared libpostproc.so so mplayer does not link to it
    shelltools.cd("libavcodec/libpostproc")
    autotools.make("SHARED_PP=yes")

def install():
    autotools.install("prefix=%s/usr \
                       BINDIR=%s/usr/bin \
                       LIBDIR=%s/usr/lib \
                       CONFDIR=%s/usr/share/mplayer \
                       DATADIR=%s/usr/share/mplayer \
                       MANDIR=%s/usr/share/man" % (get.installDIR(),
                       get.installDIR(),
                       get.installDIR(),
                       get.installDIR(),
                       get.installDIR(),
                       get.installDIR()))

    pisitools.dodir("/usr/share/mplayer/Skin")
    shelltools.copytree("default_skin", "%s/usr/share/mplayer/Skin/default" % get.installDIR())

    # Add Turkish raw fonts (though not used as default)
    pisitools.dodir("/usr/share/mplayer/fonts")
    shelltools.copytree("default_fonts", "%s/usr/share/mplayer/fonts/turkish-fonts" % get.installDIR())
    pisitools.removeDir("/usr/share/mplayer/font")
    pisitools.dosym("/usr/share/mplayer/fonts/turkish-fonts", "/usr/share/mplayer/font")

    pisitools.insinto("/etc", "etc/example.conf", "mplayer.conf")
    pisitools.insinto("/usr/share/mplayer", "etc/codecs.conf")
    pisitools.insinto("/usr/share/mplayer", "etc/input.conf")
    pisitools.insinto("/usr/share/mplayer", "etc/menu.conf")

    pisitools.dosym("/etc/mplayer.conf", "/usr/share/mplayer/mplayer.conf")
    pisitools.dodoc("AUTHORS", "ChangeLog", "README")
    pisitools.insinto("/usr/share/doc/%s/" % get.srcTAG(), "TOOLS")

    # midentify script to /usr/bin for emovix, we may also use it
    pisitools.doexe("TOOLS/midentify", "/usr/bin")
