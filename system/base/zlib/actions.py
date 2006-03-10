#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright © 2005  TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.
#
# S.Çağlar Onur <caglar@uludag.org.tr>

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import libtools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

def setup():
    autotools.rawConfigure("--shared --prefix=/usr --libdir=/lib")

def build():
    autotools.make()

def install():
    autotools.install("libdir=%s/lib" % get.installDIR())
    
    pisitools.remove("/lib/libz.a")
    pisitools.insinto("/usr/include/", "zconf.h")
    pisitools.insinto("/usr/include/", "zlib.h")

    pisitools.doman("zlib.3")
    pisitools.dodoc("FAQ", "README", "ChangeLog", "algorithm.txt")

    pisitools.dolib("libz.a")
    pisitools.dolib("libz.so.1.2.3")
   
    shelltools.chmod("%s/lib/libz.so.*" % get.installDIR())
    libtools.gen_usr_ldscript("libz.so")
