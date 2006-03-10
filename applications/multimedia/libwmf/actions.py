#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2005 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.
#
# Timu EREN <selamtux@gmail.com>

from pisi.actionsapi import get
from pisi.actionsapi import pisitools
from pisi.actionsapi import autotools

def setup():
    autotools.configure("--with-gsfontdir=/usr/share/ghostscript/fonts \
                         --with-fontdir=/usr/share/libwmf/fonts \
                         --with-docdir=/usr/share/doc/%s" % get.srcTAG() )
def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s \
                          fontdir=/usr/share/libwmf/fonts \
                          wmfonedocdir=/usr/share/doc/%s/caolan \
                          wmfdocdir=/usr/share/doc/%s" %
                          ( get.installDIR(), get.srcTAG(), get.srcTAG() ) )

    pisitools.dodoc("README", "AUTHORS", "COPYING", "CREDITS", "ChangeLog", "NEWS", "TODO")
    
