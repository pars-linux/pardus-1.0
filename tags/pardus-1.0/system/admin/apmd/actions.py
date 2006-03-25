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
from pisi.actionsapi import get

WorkDir = "apmd-3.2.1.orig"

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=\"%s\" PREFIX=/usr LIBDIR=/usr/lib" % get.installDIR())

    pisitools.dodir("/etc/apm/event.d")
    pisitools.dodir("/etc/apm/suspend.d")
    pisitools.dodir("/etc/apm/resume.d")
    pisitools.dodir("/etc/apm/other.d")
    pisitools.dodir("/etc/apm/scripts.d")
    
    pisitools.doexe("debian/apmd_proxy", "/etc/apm")
    pisitools.dodoc("AUTHORS", "apmsleep.README", "README", "debian/README.Debian", "debian/changelog*", "debian/copyright*")

    pisitools.doman("*.1", "*.8")

    # No french support
    pisitools.removeDir("/usr/share/man/fr")
