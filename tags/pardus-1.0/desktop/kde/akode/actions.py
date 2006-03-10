#!/usr/bin/python
# -*- coding: utf-8 -*- 
#
# Copyright 2005 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.
#
# S.Çağlar Onur <caglar@uludag.org.tr>

from pisi.actionsapi import pisitools
from pisi.actionsapi import kde

def setup():
    kde.configure("--with-libsamplerate \
                   --with-alsa \
                   --without-jack \
                   --with-flac \
                   --with-libmad \
                   --with-vorbis \
                   --with-speex \
                   --without-polypaudio")

def build():
    kde.make()

def install():
    kde.install()
    pisitools.dodoc("AUTHORS", "ChangeLog", "NEWS", "README")
