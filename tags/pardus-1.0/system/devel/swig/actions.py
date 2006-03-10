#!/usr/bin/python
# -*- coding: utf-8 -*- 
#
# Copyright 2005 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.
#
# S.Çağlar Onur <caglar@uludag.org.tr>

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

WorkDir = "SWIG-1.3.21"

def setup():
    pisitools.dosed("Makefile.in", "$(M4_INSTALL_DIR)", "$(DESTDIR)$(M4_INSTALL_DIR)")
                    
    autotools.configure("--with-py")

def build():
    autotools.make()

def install():
    autotools.rawInstall("install-runtime DESTDIR=%s" % get.installDIR())
    pisitools.dodoc("ANNOUNCE", "CHANGES", "FUTURE", "NEW", "README", "TODO")
