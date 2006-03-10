#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2005 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.
#
# S.Çağlar Onur <caglar@uludag.org.tr>

from pisi.actionsapi import pisitools

WorkDir = "rar"

def install():
    pisitools.insinto("/opt/rar/bin", "rar")
    pisitools.insinto("/opt/rar/lib", "default.sfx")
    pisitools.insinto("/opt/rar/etc", "rarfiles.lst")
    pisitools.dodoc("*.txt", "*.diz")
    pisitools.dosym("/opt/rar/bin/rar", "/opt/bin/rar")
