#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2005 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.
#
# Ali Erdinç Köroğlu <erdinc@erdinc.info>

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

WorkDir = "gift-0.11.8.1"

def setup():
    autotools.configure("--enable-imagemagick \
                        --enable-libvorbis")

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())
    pisitools.dodir("/usr/include/libgift")
    pisitools.dodir("/usr/share/giFT")
    shelltools.touch("%s/usr/share/giFT/giftd.log" % get.installDIR())
    pisitools.dodoc("AUTHORS", "COPYING", "ChangeLog", "INSTALL", "NEWS", "HACKING", "QUICKSTART", "README", "TODO")        
