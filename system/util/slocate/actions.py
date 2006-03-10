#!/usr/bin/python
# -*- coding: utf-8 -*- 
#
# Copyright 2005 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.
#
# Bahadır Kandemir <bahadir@haftalik.net>

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

def setup():
    autotools.configure()

def build():
    autotools.make()

def install():
    pisitools.dosed("Makefile", "-/usr/sbin/groupadd", "#-/usr/sbin/groupadd")
    pisitools.dosed("Makefile", "root.slocate", "root:slocate")
    
    pisitools.dodir("/usr/share/man/man1")

    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    pisitools.dodoc("AUTHORS", "README", "ChangeLog")
    
    pisitools.dodir("/var/lib/slocate")
    shelltools.touch("%s/var/lib/slocate/slocate.db" % get.installDIR())
    
    pisitools.remove("/usr/bin/locate")
    pisitools.remove("/usr/bin/updatedb")
    pisitools.remove("/usr/share/man/man1/locate.1.gz")

    pisitools.dosym("slocate", "/usr/bin/locate")
    pisitools.dosym("slocate", "/usr/bin/updatedb")
    pisitools.dosym("slocate.1.gz", "/usr/share/man/man1/locate.1.gz")
