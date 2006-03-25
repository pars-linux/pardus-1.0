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
from pisi.actionsapi import get

def setup():
    autotools.configure("--enable-pcmcia-support \
                        --enable-sysfs-carrier \
                        --enable-hotplug-map \
                        --disable-docbook-docs \
                        --enable-doxygen-docs \
                        --with-pid-file=/var/run/hald.pid")

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    # We install this in a seperate package to avoid gnome-python dep
    pisitools.remove("/usr/bin/hal-device-manager")

    pisitools.dodoc("AUTHORS", "COPYING", "ChangeLog", "INSTALL", "NEWS", "README")
