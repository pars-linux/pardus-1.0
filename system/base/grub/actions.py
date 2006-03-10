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
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

def setup():
    autotools.autoconf()
    autotools.aclocal()
    autotools.automake()

    shelltools.export("grub_cv_prog_objcopy_absolute", "yes")

    autotools.configure("--libdir=/lib \
                        --datadir=/usr/lib/grub \
                        --exec-prefix=/ \
                        --disable-auto-linux-mem-opt")

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    pisitools.dodoc("AUTHORS", "BUGS", "COPYING", "ChangeLog", "NEWS", "README", "THANKS", "TODO")
    pisitools.newdoc("docs/menu.lst", "grub.conf.sample")
