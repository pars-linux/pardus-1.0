#!/usr/bin/python
# -*- coding: utf-8 -*- 
#
# Copyright 2005 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.
#
# Bahadır Kandemir <bahadir@pardus.org.tr>

from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

WorkDir = "Pyrex-0.9.3"

def install():
    shelltools.system("python setup.py install --root=%s" % get.installDIR())

    pisitools.dodoc("CHANGES.txt", "INSTALL.txt", "README.txt", "USAGE.txt")
    pisitools.dohtml("Doc/*")
