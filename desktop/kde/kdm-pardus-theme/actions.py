#!/usr/bin/python
# -*- coding: utf-8 -*- 
#
# Copyright 2005 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.
#
# Gürer Özen <gurer@uludag.org.tr>

from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

WorkDir = "kdm-pardus"

def install():
    pisitools.insinto("%s/share/apps/kdm/themes/pardus/" % get.kdeDIR(), "./*")
