#!/usr/bin/python
# -*- coding: utf-8 -*- 
#
# Copyright 2005 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.
#
# S.Çağlar Onur <caglar@uludag.org.tr>

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

def setup():
    pisitools.dosed("hcid/hcid.conf", "security auto;", "security user;")
    pisitools.dosed("hcid/hcid.conf", "pin_helper /usr/bin/bluepin;", "pin_helper /etc/bluetooth/pin-helper;")
    
    pisitools.dosed("scripts/bluetooth.default", "HIDD_ENABLE=true", "HIDD_ENABLE=false")
    pisitools.dosed("scripts/bluetooth.default", "HID2HCI_ENABLE=true", "HID2HCI_ENABLE=false")

    autotools.configure("--enable-alsa \
                        --enable-cups \
                        --enable-dbus \
                        --enable-avctrl \
                        --enable-bcm203x \
                        --enable-dfutool \
                        --enable-hid2hci \
                        --enable-obex \
                        --disable-initscripts \
                        --localstatedir=/var")
def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())
    
    pisitools.dodoc("AUTHORS", "ChangeLog", "README")

    pisitools.insinto("/etc/conf.d/", "scripts/bluetooth.default", "bluetooth")

    # optional bluetooth utils
    pisitools.dosbin("tools/bccmd")
    pisitools.dosbin("tools/hcisecfilter")
    pisitools.dosbin("tools/ppporc")
    pisitools.dosbin("tools/pskey")
