# -*- coding: utf-8 -*- 
#
# Copyright 2005 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.
#
# Barış Metin <baris@uludag.org.tr>

from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

WorkDir="."
NoStrip="/"

def install():
    pisitools.dodir("/usr/share/texmf")
    pisitools.dodir("/usr/share/texmf-dist")
    
    files = shelltools.ls("*")
    # since workdir is ".", we have to be careful about pisiBuildState
    files.remove("pisiBuildState")
    for x in files:
         shelltools.copy(x, "%s/usr/share/texmf-dist/%s" % (get.installDIR(), x))

