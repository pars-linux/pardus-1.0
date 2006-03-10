#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright © 2005  TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.
#
# Gürer Özen <gurer@uludag.org.tr>

from pisi.actionsapi import pisitools
from pisi.actionsapi import get
from pisi.actionsapi.shelltools import system

WorkDir = "poster"

def setup():
    system("tar -zxf ./poster.tar.gz")
                        
def build():
    system("%s poster.c -lm -o poster" % get.CC())

def install():
    pisitools.dobin("poster")
    pisitools.dodoc("README")
    pisitools.doman("poster.1")
