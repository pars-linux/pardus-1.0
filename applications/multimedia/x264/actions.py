#!/usr/bin/python
# -*- coding: utf-8 -*- 
#
# Copyright 2005 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.
#
# İsmail Dönmez <ismail@uludag.org.tr>

from pisi.actionsapi import autotools

def setup():
    autotools.rawConfigure("--prefix=/usr \
                            --enable-pthread \
                            --enable-mp4-output")
    
def build():
    autotools.make()

def install():
    autotools.install()
    
