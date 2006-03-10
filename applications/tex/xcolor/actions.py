# -*- coding: utf-8 -*- 
#
# Copyright 2005 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.
#
# Barış Metin <baris@uludag.org.tr>

WorkDir="xcolor"

from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools

def build():
    shelltools.system("latex xcolor.ins")

def install():
    target = "/usr/share/texmf-dist/tex/latex/xcolor"
    pisitools.dodir(target)

    pisitools.insinto(target, "*.sty")
    pisitools.insinto(target, "*.def")

    target = "/usr/share/texmf-dist/dvips/xcolor"
    pisitools.dodir(target)
    pisitools.insinto(target, "*.pro")

    pisitools.dodoc("README")
