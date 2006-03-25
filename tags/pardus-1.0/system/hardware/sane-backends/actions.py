#!/usr/bin/python
# -*- coding: utf-8 -*- 
#
# Copyright 2005 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.
#
# S.Çağlar Onur <caglar@pardus.org.tr>

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

def setup():
    shelltools.export("SANEI_JPEG", "sanei_jpeg.o")
    shelltools.export("SANEI_JPEG_LO", "sanei_jpeg.lo")

    autotools.configure("--enable-libusb \
                         --with-gphoto2")

def build():
    autotools.make()

def install():
    autotools.install("docdir=%s/usr/share/doc/%s" % (get.installDIR(), get.srcTAG()))

    pisitools.dodir("/var/lib/lock/sane")

    shelltools.cd("tools/hotplug")
    pisitools.insinto("/etc/hotplug/usb", "libsane.usermap")
    pisitools.doexe("libusbscanner", "/etc/hotplug/usb")

    shelltools.echo("/etc/env.d/30sane", "SANE_CONFIG_DIR=/etc/sane.d")
