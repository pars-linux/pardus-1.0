#!/usr/bin/python
# -*- coding: utf-8 -*- 
#
# Copyright 2005 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.
#
# Barış Metin <baris@pardus.org.tr>

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools

def setup():
    shelltools.system("./autogen.sh")
    autotools.configure()

def build():
    autotools.make()

def install():
    autotools.install()
    
    pisitools.dodoc("AUTHORS", "README")

