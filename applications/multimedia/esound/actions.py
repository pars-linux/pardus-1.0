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
from pisi.actionsapi import libtools
from pisi.actionsapi import get

def setup():
    libtools.libtoolize()
    autotools.configure("--with-tcpd --with-libwrap --enable-alsa --enable-ipv6 --sysconfdir=/etc/esd")

def build():
    autotools.make()

def install():
    autotools.install("sysconfdif=%s/etc/esd" % get.installDIR())

    pisitools.dodoc("AUTHORS", "COPYING*", "ChangeLog", "README", "TODO", "NEWS", "TIPS", "docs/esound.ps")
    pisitools.dohtml("docs/html")

