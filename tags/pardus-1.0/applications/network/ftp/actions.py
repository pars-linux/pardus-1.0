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

WorkDir = "netkit-ftp-0.17"

def setup():
    autotools.rawConfigure("--prefix=/usr --enable-ssl --enable-ipv6")

def build():
    autotools.make("CC=\"%s\" LDFLAGS=\"%s\"" % (get.CC(), get.LDFLAGS()))

def install():
    pisitools.dobin("ftp/ftp")
    pisitools.doman("ftp/ftp.1", "ftp/netrc.5")
    pisitools.dodoc("ChangeLog", "README", "BUGS")
