#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright © 2005  TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.
#
# S.Çağlar Onur <caglar@uludag.org.tr>

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools

def setup():
    autotools.configure()

def build():
    autotools.make()

def install():
    pisitools.dobin("less")
    pisitools.dobin("lessecho")
    pisitools.dobin("lesskey")

    pisitools.newman("lesskey.nro", "lesskey.1")
    pisitools.newman("less.nro", "less.1")
    
    pisitools.dodoc("NEWS", "README")
