#!/usr/bin/python
# -*- coding: utf-8 -*- 
#
# Copyright 2005 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.
#
# Onur Küçük <onur@pardus.org.tr>

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

WorkDir = "hsfmodem-7.18.00.07full"

def build():
    autotools.make("all")

    # Of course make all does not compile modules, why should it...
    shelltools.cd("modules")
    autotools.make()

def install():
    autotools.rawInstall("PREFIX=%s/usr/ ROOT=%s" % (get.installDIR(), get.installDIR()))
    pisitools.insinto("/lib/modules/%s/extra" % get.curKERNEL(), "modules/*.ko")
