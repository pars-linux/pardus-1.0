#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright © 2005  TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.
#
# Timu EREN <selamtux@gmail.com>

from pisi.actionsapi import autotools
from pisi.actionsapi import shelltools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

def setup():
    pisitools.dosed("configure.in", "t=\"generic\"", "t=\"linux\"")
    shelltools.export("LDFLAGS", "%s -Wl,-z,now"  % get.LDFLAGS())
    
    autotools.autoreconf()
    
    autotools.configure()

def build():
    autotools.make("LIBS=%s" % get.LDFLAGS())

def install():
    pisitools.dodir("/usr/sbin")
    
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    shelltools.chown("%s/usr/sbin/traceroute" % get.installDIR(), "root", "wheel")
    shelltools.chmod("%s/usr/sbin/traceroute" % get.installDIR(), 04710)
    
    pisitools.doman("traceroute.8")
    pisitools.dodoc("CHANGES", "INSTALL")
