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
    shelltools.export("WANT_AUTOCONF", "2.1")
    
    autotools.autoconf()

    autotools.configure("--with-x --enable-tcpd")

def build():
    autotools.make()

def install():
    autotools.install()
    pisitools.removeDir("/usr/share/man/manm")
    
    pisitools.newman("DPS/demos/xepsf/xepsf.man", "xepsf.1")
    pisitools.newman("DPS/demos/dpsexec/dpsexec.man", "dspexec.1")
    pisitools.newman("DPS/clients/makepsres/makepsres.man", "makepsres.1")
    
    pisitools.dodoc("ANNOUNCE", "ChangeLog", "FAQ", "NEWS", "NOTES", "README", "STATUS", "TODO", "Version")
