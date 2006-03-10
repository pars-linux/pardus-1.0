#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright © 2005  TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.
#
# S.Çağlar Onur <caglar@uludag.org.tr>

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

WorkDir = "hotplug-2004_09_23"

def install():
    pisitools.doman("*.8")
    pisitools.dodoc("README", "README.modules", "ChangeLog")
    
    pisitools.insinto("/sbin", "sbin/hotplug")
    
    pisitools.insinto("/etc/hotplug", "etc/hotplug/blacklist")
    pisitools.insinto("/etc/hotplug", "etc/hotplug/hotplug.functions")
    pisitools.insinto("/etc/hotplug", "etc/hotplug/*map")

    pisitools.doexe("etc/hotplug/*.agent", "/etc/hotplug")
    pisitools.doexe("etc/hotplug/*.rc", "/etc/hotplug")
    pisitools.doexe("etc/hotplug/*.permissions", "/etc/hotplug")

    pisitools.dodir("/usr/lib/hotplug/firmware")
    pisitools.dodir("/etc/hotplug/usb")
    pisitools.dodir("/etc/hotplug/pci")
    pisitools.doexe("etc/hotplug.d/default/default.hotplug", "/etc/hotplug.d/default/")

    pisitools.dodir("/var/run/usb")
