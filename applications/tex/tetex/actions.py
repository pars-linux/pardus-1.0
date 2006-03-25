# -*- coding: utf-8 -*- 
#
# Copyright 2005 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.
#
# Barış Metin <baris@pardus.org.tr>

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

WorkDir="tetex-src-3.0"

def setup():
    install_dir = get.installDIR()
    pisitools.dodir("/usr/share/texmf")
    shelltools.sym("/usr/share/texmf-dist", "%s/usr/share/texmf-dist" % install_dir)
    autotools.rawConfigure("--prefix=%s/usr --bindir=%s/usr/bin --datadir=%s/usr/share/" %(install_dir, install_dir, install_dir))

def build():
    autotools.make("-j1 world")

def install():
    autotools.install()    
