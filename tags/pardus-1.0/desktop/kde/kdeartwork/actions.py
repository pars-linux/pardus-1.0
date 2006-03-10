#!/usr/bin/python
# -*- coding: utf-8 -*- 
#
# Copyright 2005 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.
#
# S.Çağlar Onur <caglar@uludag.org.tr>

from pisi.actionsapi import kde

def setup():
    kde.configure("--with-dpms \
                  --with-libart \
                  --with-opengl \
                  --without-xscreensaver")
                  
def build():
    kde.make()

def install():
    kde.install()
