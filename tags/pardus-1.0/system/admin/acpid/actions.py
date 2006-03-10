#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright © 2005  TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.
#
# Timu EREN <selamtux@gmail.com>

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

def build():
    pisitools.dosed("Makefile", "-Werror", "")
    autotools.make("INSTPREFIX=%s" % get.installDIR())

def install():
    pisitools.dodir("/usr/bin") #Makefile Bug
    autotools.rawInstall("INSTPREFIX=%s" % get.installDIR())

    pisitools.dodoc("Changelog", "README", "Changelog")
