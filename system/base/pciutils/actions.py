#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright © 2005  TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.
#
# S.Çağlar Onur <caglar@pardus.org.tr>

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

def setup():
    shelltools.system("./update-pciids.sh &> /dev/null")

def build():
    autotools.make("OPT=\"%s\"" % get.CFLAGS())

def install():
    pisitools.dodir("/usr/share/man")
    autotools.rawInstall("PREFIX=%s/usr" % get.installDIR())

    pisitools.dolib("lib/libpci.a")
    pisitools.dolib("lib/libpci.so")

    for f in ["config.h", "header.h", "pci.h", "types.h"]:
        pisitools.insinto("/usr/include/pci/", "lib/%s" % f)

    #pisitools.dodir("/usr/share/misc")
    #pisitools.domove("/usr/share/pci.ids", "/usr/share/misc")
