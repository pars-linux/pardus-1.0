#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2005 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.
#
# Ali Erdinç Köroğlu <erdinc@erdinc.info>

from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools

WorkDir = "skype-1.2.0.18"
    
def install():
    shelltools.move("skype", "skype.bin")
    
    pisitools.dodir("/opt/skype")
    pisitools.dodir("/opt/skype/sound")
    pisitools.dodir("/opt/skype/lang")
    
    pisitools.doexe("skype", "/opt/skype")
    pisitools.doexe("skype.bin", "/opt/skype")
    pisitools.doexe("skype-callto-handler", "/opt/skype")
    
    pisitools.insinto("/opt/skype/sound", "sound/*.wav")
    pisitools.insinto("/opt/skype/lang", "lang/*.qm")
    pisitools.insinto("/etc/dbus-1/system.d", "skype.conf")
    pisitools.insinto("/usr/share/icons/Tulliana-1.0/16x16/apps", "icons/skype_16_32.png", "skype.png") 
    pisitools.insinto("/usr/share/icons/Tulliana-1.0/32x32/apps", "icons/skype_32_32.png", "skype.png")
    pisitools.insinto("/usr/share/icons/Tulliana-1.0/48x48/apps", "icons/skype_48_32.png", "skype.png")
    pisitools.insinto("/usr/share/applications", "skype.desktop")
    
    pisitools.dosym("/opt/skype/skype", "/usr/bin/skype")
    pisitools.dodoc("README", "LICENSE")
