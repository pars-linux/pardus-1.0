#!/usr/bin/python
# -*- coding: utf-8 -*- 
#
# Copyright 2005 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.
#
# A. Murat Eren <meren@uludag.org.tr>

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get
from os import system

def install():
    pisitools.insinto("/usr/share/fonts/%s" % get.srcNAME(), "*.ttf")
    system("mkfontscale")
    system("mkfontdir")
    pisitools.insinto("/usr/share/fonts/%s" % get.srcNAME(), "fonts*")
    pisitools.dodoc("COPYRIGHT.TXT", "README.TXT", "RELEASENOTES.TXT")
