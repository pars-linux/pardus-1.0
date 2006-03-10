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
from pisi.actionsapi import shelltools
from pisi.actionsapi import coreutils
from pisi.actionsapi import get

def setup():
    shelltools.export("LDFLAGS", get.LDFLAGS() + "-Wl,-z,now")
    pisitools.dosed("src/Makefile.in", "LDFLAGS = -s", "LDFLAGS = %s" % get.LDFLAGS())

    shelltools.export("BUILD_CC", get.CC())
    autotools.rawConfigure("-confdir=/etc +sgid +fhs +lang all")

def build():
    autotools.make()

def install():
    autotools.rawInstall("PREFIX=%s" % get.installDIR())
    
    pisitools.dosym("man", "/usr/bin/manpath")

    pisitools.dodoc("LSM", "README*", "TODO")

    pisitools.dodir("/var/cache/man")

    list = (coreutils.cat(get.installDIR() + "/etc/man.conf") | coreutils.grep("^MANSECT") | coreutils.join).split()[1]
    
    for index in list.split(":"):
        pisitools.dodir("/var/cache/man/cat%s" % index)
        shelltools.chmod("%s/var/cache/man/cat%s" % (get.installDIR(),index), 0775)
        shelltools.chown("%s/var/cache/man/cat%s" % (get.installDIR(),index), "root", "man")
