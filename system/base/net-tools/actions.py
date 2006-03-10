#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright © 2005  TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.
#
# S.Çağlar Onur <caglar@uludag.org.tr>

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

def setup():
    pisitools.dosed("Makefile", "(?m)^(COPTS =.*)", "COPTS =" + get.CFLAGS())
    pisitools.dosed("Makefile", "(?m)^(LOPTS =.*)", "LOPTS =" + get.LDFLAGS())
                    
def build():
    autotools.make("libdir")
    autotools.make()
    autotools.make("ether-wake")
    autotools.make("i18ndir")

def install():
    autotools.rawInstall("BASEDIR=%s" % get.installDIR())

    pisitools.dosbin("ether-wake")
    pisitools.dosym("/bin/hostname", "/usr/bin/hostname")

    pisitools.dodoc("README", "README.ipv6", "TODO")
