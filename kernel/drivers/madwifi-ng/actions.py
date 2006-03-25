#!/usr/bin/python
# -*- coding: utf-8 -*- 
#
# Copyright 2005 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.
#
# Onur Küçük <onur@pardus.org.tr>

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

WorkDir = "madwifi-ng-r1365-20051222"

def setup():
    for dir in ["ath", "ath_hal", "net80211", "ath_rate/amrr", "ath_rate/onoe", "ath_rate/sample"]:
        pisitools.dosed("%s/Makefile" % dir, "SUBDIRS=", "M=")

    pisitools.dosed("net80211/ieee80211_ioctl.h", ".*if.h>")

    pisitools.dosed("tools/athstats.c", "err(1, ifr.ifr_name);", "err(1, \"%s\", ifr.ifr_name);")
    pisitools.dosed("tools/Makefile", "CFLAGS=", "CFLAGS+=")
    pisitools.dosed("tools/Makefile", "LDFLAGS=", "LDFLAGS+=")

def build():
    shelltools.export("KERNELPATH", "/usr/src/linux")
    shelltools.export("TARGET", "i386-elf")
    shelltools.export("TOOLPREFIX", "/usr/bin/")
    shelltools.export("KERNELRELEASE", get.curKERNEL())
    
    autotools.make("all")

def install():
    autotools.rawInstall("DESTDIR=%s BINDIR=/usr/bin MANDIR=/usr/share/man" % get.installDIR())
    pisitools.domove("/usr/bin/wlanconfig", "/sbin")

    pisitools.dodoc("README", "COPYRIGHT", "docs/users-guide.pdf", "docs/WEP-HOWTO.txt")

    # install headers for use by wpa_supplicant and hostapd
    pisitools.insinto("/usr/include/madwifi/include/","include/*.h")
    pisitools.insinto("/usr/include/madwifi/net80211", "net80211/*.h")
