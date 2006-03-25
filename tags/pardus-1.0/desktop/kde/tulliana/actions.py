#!/usr/bin/python
# -*- coding: utf-8 -*- 
#
# Copyright 2005 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.
#
# S.Çağlar Onur <caglar@pardus.org.tr>

from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

WorkDir = "Tulliana-1.0"

def install():
    pisitools.dodir("/usr/share/icons/Tulliana-1.0")

    for dir in ("128x128", "64x64", "48x48", "32x32", "22x22", "16x16", "extra"):
        shelltools.copytree(dir, "%s/usr/share/icons/Tulliana-1.0/%s" % (get.installDIR(), dir))

    pisitools.insinto("/usr/share/icons/Tulliana-1.0", "author")
    pisitools.insinto("/usr/share/icons/Tulliana-1.0", "index.theme")
    pisitools.insinto("/usr/share/icons/Tulliana-1.0", "license.txt")
    pisitools.insinto("/usr/share/icons/Tulliana-1.0", "readme.txt")
    pisitools.insinto("/usr/share/icons/Tulliana-1.0", "thanks.to")
