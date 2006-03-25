#!/usr/bin/python
# -*- coding: utf-8 -*- 
#
# Copyright 2005 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.
#
# İsmail Dönmez <ismail@pardus.org.tr>

from pisi.actionsapi import autotools
from pisi.actionsapi import shelltools

WorkDir="fftw-2.1.5"

def setup():
    shelltools.export("LDFLAGS","-L/usr/lib/gcc/i686-pc-linux-gnu/")   
    autotools.configure("--enable-shared \
                         --enable-threads \
                         --enable-i386-hacks \
                         --disable-static")
def build():
    autotools.make()
def install():
    autotools.install()
