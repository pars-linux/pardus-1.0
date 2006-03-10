# -*- coding: utf-8 -*- 
#
# Copyright 2005 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.
#
# Barış Metin <baris@uludag.org.tr>


from pisi.actionsapi import pisitools

def install():
    target = "/usr/share/texmf-dist/latex-beamer"
    pisitools.dodir(target)

    pisitools.insinto(target, "base")
    pisitools.insinto(target, "emulation")
    pisitools.insinto(target, "extensions")
    pisitools.insinto(target, "themes")

    # FIXME: 
    # install lyx and emacs files
    # install docs...


