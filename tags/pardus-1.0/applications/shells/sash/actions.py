#!/usr/bin/python
# -*- coding: utf-8 -*- 
#
# Copyright 2005 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.
#
# İsmail Dönmez <ismail@uludag.org.tr>

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools

def build():
    autotools.make()
    
def install():
    pisitools.dobin("sash","/bin")

    pisitools.dodoc("CHANGES", "README")

