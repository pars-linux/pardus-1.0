#!/usr/bin/python
# -*- coding: utf-8 -*- 
#
# Copyright 2005 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.
#
# S.Çağlar Onur <caglar@uludag.org.tr>

from pisi.actionsapi import kde
from pisi.actionsapi import get
from pisi.actionsapi import shelltools

WorkDir = "arts-1.5.0"

def setup():
    kde.configure("--enable-alsa \
                  --enable-vorbis \
                  --enable-libmad \
                  --with-audiofile \
                  --with-nas \
                  --without-jack \
                  --without-esd \
                  --without-mas")

def build():
    kde.make()

def install():
    kde.install()
    # Suid ARts, possible fix of http://bugs.uludag.org.tr/show_bug.cgi?id=262
    shelltools.chmod("%s/bin/artswrapper" % get.kdeDIR(), 04755)
