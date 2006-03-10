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

def install():
    pythonmodules.install()

    pisitools.remove("%s/bin/pisi-kga" % get.kdeDIR())
    pisitools.dosym("%s/share/apps/pisi_kga/PisiKga.py" % get.kdeDIR(), "%s/bin/pisi-kga" % get.kdeDIR())
