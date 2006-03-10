#!/usr/bin/python
# -*- coding: utf-8 -*- 
#
# Copyright 2005 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.
#
# Gökçen Eraslan <gokcene@anadolu.edu.tr>

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

WorkDir = "dhcpcd-1.3.22-pl4"

def setup():
    pisitools.dosed("configure", " -march=i.86")
    pisitools.dosed("dhcpconfig.c", "/etc/ntp\.drift", "/var/lib/ntp/ntp.drift")
    autotools.rawConfigure(" --prefix=\"\" \
                             --sysconfdir=/var/lib \
                             --mandir=/usr/share/man")

def build():
    autotools.make()

def install():
    autotools.install("sbindir=%s/sbin" % get.installDIR())
    pisitools.removeDir("/etc/dhcpc")
    pisitools.dodoc ("AUTHORS", "ChangeLog", "NEWS", "README")
