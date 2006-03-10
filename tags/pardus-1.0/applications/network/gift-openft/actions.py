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
from pisi.actionsapi import get

WorkDir = "gift-openft-0.2.1.6"

def setup():
    autotools.configure()
    
def build():
    autotools.make()
    
def install():
    autotools.rawInstall("DESTDIR=%s giftconfdir='/etc/giFT' \
                                     plugindir='/usr/lib/giFT' \
                                     datadir='/usr/share/giFT' \
                                     giftperldir='/usr/bin' \
                                     includedir='/usr/include/libgift'" % get.installDIR())
    pisitools.dodoc("README", "NEWS", "ChangeLog", "TODO")
