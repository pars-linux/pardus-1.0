#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright © 2005  TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.
#
# S.Çağlar Onur <caglar@uludag.org.tr>

from pisi.actionsapi import shelltools
from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

def setup():
    pisitools.dosed("lsusb.8", "/usr/share/usb.ids", "/usr/share/misc/usb.ids")
    shelltools.system("sed -e '/^DEST=/s:=usb.ids:=/usr/share/misc/usb.ids:' \
                                  update-usbids.sh > update-usbids")
    shelltools.system("./update-usbids.sh &> /dev/null")

    autotools.configure("--datadir=/usr/share/misc \
                         --enable-usbmodules")

def build():
    autotools.make()
    
def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    pisitools.dosbin("update-usbids")
    pisitools.dodoc("AUTHORS", "ChangeLog", "NEWS", "README")
