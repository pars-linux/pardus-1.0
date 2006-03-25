#!/usr/bin/python
# -*- coding: utf-8 -*- 
#
# Copyright 2005 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.
#
# S.Çağlar Onur <caglar@pardus.org.tr>

from pisi.actionsapi import kde
from pisi.actionsapi import get
from pisi.actionsapi import shelltools

def setup():
    shelltools.export("DO_NOT_COMPILE", "mpeglib mpeglib_artsplug kaboodle noatun")
    kde.configure("--with-extra-includes=/usr/include/speex \
                   --with-akode \
                   --with-cdparanoia \
                   --enable-cdparanoia \
                   --with-arts-alsa \
                   --with-alsa \
                   --with-vorbis \
                   --with-lame \
                   --with-flac \
                   --with-speex \
                   --with-libmad \
                   --without-jack \
                   --with-xine \
                   --with-musicbrainz")
                                            
def build():
    kde.make()

def install():
    kde.install()
