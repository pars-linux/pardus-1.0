# -*- coding: utf-8 -*- 
#
# Copyright 2005 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.
#
# Barış Metin <baris@uludag.org.tr>

from pisi.actionsapi import pisitools

def install():
    target = "/usr/share/texmf-dist/tex/"
    pisitools.dodir(target)

    pisitools.insinto(target, "latex")
    pisitools.insinto(target, "generic")
    pisitools.insinto(target, "plain")

