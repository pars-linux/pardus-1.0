#!/usr/bin/python
# -*- coding: utf-8 -*- 
#
# Copyright 2005 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.
#
# S.Çağlar Onur <caglar@uludag.org.tr>

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

WorkDir = "Grounation-0.3"

def install():
    pisitools.insinto("/usr/share/cursors/xorg-x11/Grounation/cursors/", "Grounation/cursors/*")
    pisitools.insinto("/usr/share/cursors/xorg-x11/Grounation-left/cursors/", "Grounation-left/cursors/*")
