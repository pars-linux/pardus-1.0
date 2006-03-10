#!/usr/bin/python
# -*- coding: utf-8 -*- 
#
# Copyright 2005 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.
#
# A. Murat Eren <meren@uludag.org.tr>

from pisi.actionsapi import pisitools
from pisi.actionsapi import autotools
from pisi.actionsapi import get

libdir = "/usr/lib/hevea"
bindir = "/usr/bin"

def build():
    autotools.make("BINDIR=%s LIBDIR=%s" % (bindir, libdir))

def install():
    pisitools.dodir(libdir)
    pisitools.dodir(bindir)
    autotools.rawInstall("BINDIR=%s LIBDIR=%s" % \
                          (get.installDIR() + bindir, \
                           get.installDIR() + libdir))

    pisitools.dodoc("README", "CHANGES", "LICENSE")
