#!/usr/bin/python
# -*- coding: utf-8 -*- 
#
# Copyright 2005 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.
#
# Onur Küçük <onur@uludag.org.tr>

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

def setup():
    autotools.configure()

def build():
    autotools.make("setserial")

def install():
    pisitools.doman("setserial.8")
    pisitools.dobin("setserial", "/bin")

    pisitools.insinto("/etc", "serial.conf")
    pisitools.dodoc("README")
    pisitools.dodir("/usr/share/doc/%s/txt" % get.srcTAG())
    pisitools.insinto("/usr/share/doc/%s/txt" % get.srcTAG(), "Documentation/*")

