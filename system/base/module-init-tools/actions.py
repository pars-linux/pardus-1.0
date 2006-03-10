#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright © 2005  TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.
#
# A. Murat Eren <meren@uludag.org.tr>

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

def setup():
    shelltools.unlink("missing")
    
    shelltools.export("WANT_AUTOMAKE", "1.6")
    
    autotools.automake("--add-missing")
    autotools.configure("--prefix=/ --enable-zlib")

def build():
    autotools.make()

def install():
    autotools.install("prefix=%s" % get.installDIR())
    pisitools.dosym("../bin/lsmod", "/sbin/lsmod")

    pisitools.dosbin("generate-modprobe.conf", "/sbin")
    pisitools.dodir("/etc")

    pisitools.doman("*.[1-8]")  

    pisitools.dodoc("AUTHORS", "ChangeLog", "INSTALL", "NEWS", "README", "TODO")
