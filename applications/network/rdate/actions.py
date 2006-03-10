#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright © 2005  TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.
#
# Ahmet AYGÜN <ahmet@zion.gen.tr>

from pisi.actionsapi import autotools
from pisi.actionsapi import get
from pisi.actionsapi import pisitools

WorkDir="rdate-990821"

def build():
    autotools.make("CFLAGS=\"%s\" LDFLAGS=\"%s\"" % (get.CFLAGS(), get.LDFLAGS()))

def install():
    pisitools.dodir("/usr/bin")
    pisitools.dodir("/usr/share/man/man1")
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())
    pisitools.dodoc("README.linux")
