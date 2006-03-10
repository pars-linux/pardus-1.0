#!/usr/bin/python
# -*- coding: utf-8 -*- 
#
# Copyright 2005 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.
#
# Fatih Aşıcı <fasici@linux-sevenler.org>

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

WorkDir = "xc/lib/Xaw3d"

def setup():
    pisitools.dosed("Imakefile", "#.*EXTRA_DEFINES", "EXTRA_DEFINES")

def build():
    shelltools.makedirs("X11")
    shelltools.cd("X11")
    shelltools.system("ln -sf ../../Xaw3d .")
    shelltools.cd("../")
    shelltools.system("xmkmf")
    autotools.make("includes")
    autotools.make("depend")
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s install" % get.installDIR())
    pisitools.dodoc("README.XAW3D")

