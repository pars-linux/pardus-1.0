#!/usr/bin/python
# -*- coding: utf-8 -*- 
#
# Copyright 2005 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.
#
# İsmail Dönmez <ismail@pardus.org.tr>

from pisi.actionsapi import autotools

WorkDir="mpeg2dec-0.4.0"

def setup():
    autotools.configure("--enable-shared \
                         --disable-sdl \
                         --disable-static \
                         --without-x")

def build():
    autotools.make()

def install():
    autotools.install()
    
