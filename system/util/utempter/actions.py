#!/usr/bin/python
# -*- coding: utf-8 -*- 
#
# Copyright 2005 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.
#
# S.Çağlar Onur <caglar@pardus.org.tr>

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

WorkDir = "utempter-0.5.5"

def setup():
    shelltools.export("LDFLAGS", "%s -Wl,-z,now" % get.LDFLAGS())

def build():
    autotools.make("RPM_OPT_FLAGS=\"%s\"" % get.CFLAGS())

def install():
    autotools.rawInstall("RPM_BUILD_ROOT=\"%s\" \
                         LIBDIR=/usr/lib" % get.installDIR())
    pisitools.dobin("utmp")
