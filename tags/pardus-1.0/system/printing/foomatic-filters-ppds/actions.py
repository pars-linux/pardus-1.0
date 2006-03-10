#!/usr/bin/python
# -*- coding: utf-8 -*- 
#
# Copyright 2005 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.
#
# Onur Küçük <onur@uludag.org.tr>

from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

def install():
    shelltools.system("./install -d %s -p /usr -z" % get.installDIR())
    pisitools.dodir("/usr/share/cups/model")
    pisitools.dosym("/usr/share/ppd", "/usr/share/cups/model/foomatic-ppds")

