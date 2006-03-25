#!/usr/bin/python
# -*- coding: utf-8 -*- 
#
# Copyright 2005 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.
#
# Onur Küçük <onur@pardus.org.tr>

from pisi.actionsapi import autotools
from pisi.actionsapi import shelltools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

WorkDir = "rt2500-1.1.0-b3"

def build():
    shelltools.export("BUILD_PARAMS", "-C /usr/src/linux-%s" % get.curKERNEL())
    shelltools.cd("Module")
    autotools.make("KERNDIR=/lib/modules/%s/build" % get.curKERNEL())

def install():
    shelltools.cd("Module")
    pisitools.insinto("/etc/Wireless/RT2500STA", "Module/RT2500STA.dat")
    pisitools.dodoc("Module/README", "Module/TESTING", "Module/iwpriv_usage.txt", "THANKS", "FAQ", "CHANGELOG")
    pisitools.insinto("/lib/modules/%s/extra" % get.curKERNEL(), "rt2500.ko")
