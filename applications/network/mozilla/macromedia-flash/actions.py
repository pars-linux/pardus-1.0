#!/usr/bin/python
# -*- coding: utf-8 -*- 
#
# Copyright 2005 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.
#
# S.Çağlar Onur <caglar@uludag.org.tr>

from pisi.actionsapi import pisitools

WorkDir = "install_flash_player_7_linux"
NoStrip = "/"

def install():
    pisitools.doexe("libflashplayer.so", "/opt/netscape/plugins")
    pisitools.insinto("/opt/netscape/plugins", "flashplayer.xpt")
   
    pisitools.dodir("/usr/lib/nsbrowser/plugins")
    pisitools.dosym("/opt/netscape/plugins/libflashplayer.so", "/usr/lib/nsbrowser/plugins/libflashplayer.so")
    pisitools.dosym("/opt/netscape/plugins/flashplayer.xpt", "/usr/lib/nsbrowser/plugins/flashplayer.xpt")

    pisitools.dodoc("Readme.txt")
