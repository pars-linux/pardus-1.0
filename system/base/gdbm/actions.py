#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright © 2005  TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.
#
# S.Çağlar Onur <caglar@pardus.org.tr>

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

def setup():
    autotools.configure()
            
def build():
    #sed -i '/HAVE_LIBNDBM/s:.*::' autoconf.h
    autotools.make()

def install():
    autotools.rawInstall("INSTALL_ROOT=%s" % get.installDIR())
    
    autotools.rawInstall("includedir=/usr/include/gdbm INSTALL_ROOT=%s" % get.installDIR(), "install-compat")
    pisitools.dodoc("ChangeLog", "NEWS", "README")

    #temp backwards support
    if shelltools.can_access_file("/usr/lib/libgdbm.so.2"):
        shelltools.copy("/usr/lib/libgdbm.so.2", "%s/usr/lib/" % get.installDIR())
        shelltools.touch("%s/usr/lib/libgdbm.so.2" % get.installDIR())
