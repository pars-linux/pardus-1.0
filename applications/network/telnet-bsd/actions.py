#!/usr/bin/python
# -*- coding: utf-8 -*- 
#
# Copyright 2005 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.
#
# Gökçen Eraslan <gokcene@anadolu.edu.tr>

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

def setup():
    pisitools.dosed("po/Makefile.in.in", "destdir=", "destdir=$(DESTDIR)")
    autotools.configure("--enable-nls")
    
def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())
    pisitools.dodoc("README", "THANKS", "NEWS", "AUTHORS", "ChangeLog", "INSTALL")
    pisitools.remove("/usr/share/man/man8/in.telnetd.8")
    pisitools.remove("/usr/share/man/man8/telnetd.8")
                     
