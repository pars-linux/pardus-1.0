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
    shelltools.touch("man/Makefile.am")
    shelltools.touch("man/texinfo2man.c")
    autotools.configure("--enable-nls")

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())
    pisitools.dodoc("AUTHORS", "NEWS", "README*")
    # Move HTML content into proper directory
    pisitools.dohtml("%s/usr/doc/indent/" % get.installDIR())
    # Remove no-needed directory
    pisitools.removeDir("/usr/doc")
