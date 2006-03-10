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
from pisi.actionsapi import shelltools

def setup():
    pisitools.dosed("MCONFIG", "(?m)^(HAVE_PAM=.*)no", r"\1yes")
    pisitools.dosed("MCONFIG", "(?m)^(HAVE_KILL=.*)no", r"\1yes")
    pisitools.dosed("MCONFIG", "(?m)^(HAVE_SLN=.*)no", r"\1yes")
    pisitools.dosed("MCONFIG", "(?m)^(HAVE_TSORT.*)no", r"\1yes")
    pisitools.dosed("MCONFIG", "-pipe -O2 \$(CPUOPT) -fomit-frame-pointer", "${CFLAGS}")
    pisitools.dosed("MCONFIG", "CPU=.*", "CPU=${CHOST%%-*}")
    pisitools.dosed("MCONFIG", "usr/man", "usr/share/man")
    pisitools.dosed("MCONFIG", "usr/info", "usr/share/info")
    pisitools.dosed("MCONFIG", "SUIDMODE=.*4755", "SUIDMODE=4711")

    shelltools.export("LDFLAGS", "%s -Wl,-z,now" % get.LDFLAGS())
    shelltools.export("CC", get.CC())

    autotools.configure()
    
def build():
    autotools.make()

    shelltools.cd("partx/")

    shelltools.export("CFLAGS", "%s -include linux/compiler.h" % get.CFLAGS())
    autotools.make("CFLAGS=\"${CFLAGS}\"")

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    pisitools.dosbin("partx/addpart")
    pisitools.dosbin("partx/delpart")
    pisitools.dosbin("partx/partx")

    pisitools.dodoc("HISTORY", "MAINTAINER", "README", "VERSION", "example.files/*")
