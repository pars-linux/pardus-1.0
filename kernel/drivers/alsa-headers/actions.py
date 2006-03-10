#!/usr/bin/python
# -*- coding: utf-8 -*- 
#
# Copyright 2005 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.
#
# S.Çağlar Onur <caglar@uludag.org.tr>

from pisi.actionsapi import pisitools

WorkDir = "alsa-driver-1.0.10"

def install():
    pisitools.insinto("/usr/include/sound/", "alsa-kernel/include/*.h")
