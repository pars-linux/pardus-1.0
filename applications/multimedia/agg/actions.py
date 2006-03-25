#!/usr/bin/python
# -*- coding: utf-8 -*- 
#
# Copyright 2005 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.
#
# İsmail Dönmez <ismail@pardus.org.tr>

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools

WorkDir="agg23"

def setup():
    shelltools.system("chmod +x autogen.sh")
    shelltools.system("./autogen.sh --prefix=/usr")

def build():
    autotools.make()
    
def install():
    autotools.install()

    pisitools.dodoc("ChangeLog", "README.txt")
