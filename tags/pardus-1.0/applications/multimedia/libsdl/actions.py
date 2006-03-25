#!/usr/bin/python
# -*- coding: utf-8 -*- 
#
# Copyright 2005 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.
#
# A. Murat Eren <meren@pardus.org.tr>

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import libtools
from pisi.actionsapi import get

WorkDir = "SDL-1.2.7"

def setup():
    pisitools.dosed("configure.in", "-laudio", "-laudio -L/usr/lib")
    shelltools.system("./autogen.sh")

    autotools.configure("--enable-events \
                         --enable-cdrom \
                         --enable-threads \
                         --enable-timers \
                         --enable-endian \
                         --enable-file \
                         --disable-oss \
                         --enable-alsa \
                         --disable-esd \
                         --enable-arts \
                         --enable-nas \
                         --enable-nasm \
                         --enable-video-x11 \
                         --disable-dga \
                         --enable-video-x11-xv \
                         --enable-video-x11-xinerama \
                         --disable-video-dga \
                         --enable-video-fbcon \
                         --disable-video-ggi \
                         --disable-video-svga \
                         --enable-video-aalib \
                         --enable-video-caca \
                         --enable-video-opengl \
                         --enable-video-dummy \
                         --disable-video-directfb")

def build():
    autotools.make()

def install():
    autotools.install()
    libtools.preplib()

    pisitools.dosed("%s/usr/lib/libSDL.la" % get.installDIR(), "-pthread", " ")
    pisitools.dodoc("BUGS", "CREDITS", "README", "README-SDL.txt",\
                    "README.CVS", "TODO", "WhatsNew")
    pisitools.dohtml("./")
