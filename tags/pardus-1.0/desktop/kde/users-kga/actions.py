#!/usr/bin/python
# -*- coding: utf-8 -*- 
#
# Copyright 2005 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.
#
# İsmail Dönmez <ismail@uludag.org.tr>

from pisi.actionsapi import pythonmodules
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

WorkDir = "user-kga-0.1"

def install():
    pythonmodules.install()
    pisitools.remove("%s/bin/users-kga" % get.kdeDIR())
    pisitools.dosym("%s/share/apps/users_kga/users_kga.py" % get.kdeDIR(), "%s/bin/users-kga" % get.kdeDIR())
