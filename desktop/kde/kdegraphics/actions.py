#!/usr/bin/python
# -*- coding: utf-8 -*- 
#
# Copyright 2005 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.
#
# S.Çağlar Onur <caglar@uludag.org.tr>

from pisi.actionsapi import kde
from pisi.actionsapi import shelltools

def setup():
    # For world domination and the rest...
    shelltools.export("DO_NOT_COMPILE", "kpovmodeler kmrml kview kuickshow")

    kde.configure("--with-poppler \
                   --with-kamera \
                   --with-imlib \
                   --without-openexr")
                  
def build():
    kde.make()

def install():
    kde.install()
