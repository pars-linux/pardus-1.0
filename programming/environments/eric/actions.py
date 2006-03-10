#!/usr/bin/python
# -*- coding: utf-8 -*- 
#
# Copyright 2005 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.
#
# Gürer Özen <gurer@uludag.org.tr>

from pisi.actionsapi import pisitools
from pisi.actionsapi.pythonmodules import run
from pisi.actionsapi import get

def install():
    pisitools.dodoc("HISTORY", "LICENSE.GPL", "THANKS", "eric/README*")
    bdir = "/usr/bin"
    idir = get.installDIR()
    ddir = "/usr/lib/%s/site-packages" % get.curPYTHON()
    run("install.py -b %s -i %s -d %s -c" % (bdir, idir, ddir))
