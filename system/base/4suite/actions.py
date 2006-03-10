#!/usr/bin/python
# -*- coding: utf-8 -*- 
#
# Copyright © 2005  TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.
#
# Barış Metin <baris@uludag.org.tr>

from pisi.actionsapi import pythonmodules
from pisi.actionsapi import get

WorkDir="4Suite-1.0b2"

def setup():
    pythonmodules.run("setup.py config --prefix=/usr --docdir=/usr/share/doc/%s" % get.srcTAG())

def build():
    pythonmodules.compile()

def install():
    pythonmodules.install()
