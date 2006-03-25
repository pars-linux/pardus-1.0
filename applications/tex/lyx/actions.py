# -*- coding: utf-8 -*- 
#
# Copyright 2005 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.
#
# Gürer Özen <gurer@pardus.org.tr>

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

#WorkDir="tetex-src-3.0"

def setup():
    autotools.rawConfigure("--prefix=%s/usr --with-frontend=qt --with-qt-dir=%s" % (get.installDIR(), get.qtDIR()))

def build():
    autotools.make()

def install():
    autotools.install()
    pisitools.dodoc("README*", "UPGRADING", "INSTALL*", "ChangeLog", "NEWS",
        "COPYING", "ANNOUNCE", "ABOUT-NLS" )
