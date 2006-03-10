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
from pisi.actionsapi import libtools
from pisi.actionsapi import get

WorkDir = "libxml++-1.0.4"

def setup():
    shelltools.export("WANT_AUTOCONF", "2.5") 
    shelltools.export("WANT_AUTOMAKE", "1.7") 
    
    autotools.aclocal()
    autotools.autoconf()
    autotools.automake("-a")
    
    libtools.libtoolize("--force --copy")
    
    autotools.configure()

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())
    pisitools.dodoc("ChangeLog", "AUTHORS", "NEWS", "README*")
