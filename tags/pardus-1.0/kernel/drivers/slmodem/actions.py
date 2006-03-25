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
from pisi.actionsapi import get

def setup():
    pisitools.dosed("drivers/Makefile", "SUBDIRS=\$(shell pwd)", "SUBDIRS=%s/drivers" % get.srcDIR())
    pisitools.dosed("drivers/Makefile", "SUBDIRS=", "M=")

    pisitools.dosed("modem/Makefile", " -O")
    pisitools.dosed("modem/Makefile", "LFLAGS", "LDFLAGS")
    pisitools.dosed("modem/Makefile", "^slmodemd: -lasound$")

def build():
    autotools.make("SUPPORT_ALSA=1 modem")
    autotools.make("KERNEL_DIR=/usr/src/linux drivers")

def install():
    pisitools.insinto("/lib/modules/%s/extra" % get.curKERNEL(), "drivers/*.ko")
    pisitools.insinto("/usr/sbin", "modem/modem_test", "slmodem_test")
    pisitools.dosbin("modem/slmodemd")
    pisitools.dodir("/var/lib/slmodem")

    pisitools.dodoc("Changes", "README")

