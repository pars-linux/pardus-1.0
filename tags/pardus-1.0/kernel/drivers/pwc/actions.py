#!/usr/bin/python
# -*- coding: utf-8 -*- 
#
# Copyright 2005 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.
#
# Onur Küçük <onur@uludag.org.tr>

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

def build():
    shelltools.export("ARCH", "i386")
    autotools.make("KSRC=/usr/src/linux")

def install():
    pisitools.insinto("/lib/modules/%s/kernel/drivers/usb/media/pwc" % get.curKERNEL(), "pwc.ko")
