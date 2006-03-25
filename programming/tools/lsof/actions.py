#!/usr/bin/python
# -*- coding: utf-8 -*- 
#
# Copyright 2005 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.
#
# S.Çağlar Onur <caglar@pardus.org.tr>

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

WorkDir = "lsof_4.75_src"

def setup():
    shelltools.touch(".neverInv")
    shelltools.system("./Configure linux")

def build():
    autotools.make("all")

def install():
    pisitools.dosbin("lsof")
    pisitools.dolib("lib/liblsof.a")

    pisitools.insinto("/usr/share/lsof/scripts", "scripts/*")

    pisitools.doman("lsof.8")
    pisitools.dodoc("00*")
