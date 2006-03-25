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

WorkDir = "xvidcore-1.0.2"

def setup():
    shelltools.cd("build/generic")
    autotools.configure()

def build():
    shelltools.cd("build/generic")
    autotools.make()

def install():
    shelltools.cd("build/generic")
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    shelltools.cd("../../")

    pisitools.dodoc("AUTHORS", "ChangeLog", "README", "TODO", "doc/*")

    pisitools.dosym("libxvidcore.so.4.0",  "/usr/lib/libxvidcore.so")
    pisitools.dosym("libxvidcore.so.4.0",  "/usr/lib/libxvidcore.so.4")
    pisitools.dodoc("CodingStyle", "doc/README", "examples/*")
