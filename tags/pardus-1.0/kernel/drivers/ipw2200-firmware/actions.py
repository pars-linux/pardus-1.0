#!/usr/bin/python
# -*- coding: utf-8 -*- 
#
# Copyright 2005 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.
#
# S.Çağlar Onur <caglar@uludag.org.tr>

from pisi.actionsapi import pisitools

WorkDir = "."

def install():
    pisitools.insinto("/lib/firmware", "*.fw")
    pisitools.insinto("/lib/firmware", "LICENSE", "ipw-2.4-LICENSE")

    # Kludge, remove when we update to 2.6.15 kernel
    pisitools.dosym("/lib/firmware/ipw-2.4-boot.fw","/lib/firmware/ipw-2.2-boot.fw")
    pisitools.dosym("/lib/firmware/ipw-2.4-bss.fw", "/lib/firmware/ipw-2.2-bss.fw")
    pisitools.dosym("/lib/firmware/ipw-2.4-bss_ucode.fw", "/lib/firmware/ipw-2.2-bss_ucode.fw")
    pisitools.dosym("/lib/firmware/ipw-2.4-ibss.fw", "/lib/firmware/ipw-2.2-ibss.fw")
    pisitools.dosym("/lib/firmware/ipw-2.4-ibss_ucode.fw", "/lib/firmware/ipw-2.2-ibss_ucode.fw")
    pisitools.dosym("/lib/firmware/ipw-2.4-sniffer.fw", "/lib/firmware/ipw-2.2-sniffer.fw")
    pisitools.dosym("/lib/firmware/ipw-2.4-sniffer_ucode.fw", "/lib/firmware/ipw-2.2-sniffer_ucode.fw")
