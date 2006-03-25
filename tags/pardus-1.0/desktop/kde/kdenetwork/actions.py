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
from pisi.actionsapi import pisitools

def setup():
    shelltools.export("DO_NOT_COMPILE", "ksirc")

    kde.configure("--with-slp \
                   --with-wifi \
                   --disable-sametime-plugin \
                   --without-xmms \
                   --without-external-libgadu")
                  
def build():
    kde.make()

def install():
    kde.install()

    shelltools.chmod("%s/bin/reslisa" % get.kdeDIR(), 04755)
    pisitools.dodir("/etc")
    shelltools.touch("%s/etc/lisarc" % get.installDIR())                     
