#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright © 2005  TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.
#
# A. Murat Eren <meren@pardus.org.tr>

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools

#FIXME: Bu paketin preInst gorevleri var..

def setup():
    shelltools.export("CFLAGS", "")
    shelltools.export("CXXFLAGS", "")
    autotools.configure()

def build():
    autotools.make()

def install():
    autotools.install()
    pisitools.dodoc("ChangeLog", "AUTHORS", "NEWS", "README", "COPYING", "INSTALL")
    pisitools.dosym("libdvdcss.so.2.0.7", "/usr/lib/libdvdcss.so.0")
    pisitools.dosym("libdvdcss.so.2.0.7", "/usr/lib/libdvdcss.so.1")
