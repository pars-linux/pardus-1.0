#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright © 2005  TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.
#
# A. Murat Eren <meren@pardus.org.tr>

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

def setup():

    autotools.rawConfigure("-prefix /usr \
                            -bindir /usr/bin \
                            -libdir /usr/lib/ocaml \
                            -mandir /usr/share/man \
                            --with-pthread \
                            -no-tk")

    pisitools.dosed("config/Makefile", "\(BYTECCCOMPOPTS=.*\)", "\1 %s" % (get.CFLAGS()))
    pisitools.dosed("config/Makefile", "\(NATIVECCCOMPOPTS=.*\)", "\1 %s" % (get.CFLAGS()))

def build():
    autotools.make("world")
    autotools.make("opt")
    autotools.make("opt.opt")
    
def install():
    autotools.rawInstall("BINDIR=%(install)s/usr/bin \
                          LIBDIR=%(install)s/usr/lib/ocaml \
                          MANDIR=%(install)s/usr/share/man" \
                          % { "install": get.installDIR()})


    pisitools.dosed("/usr/lib/ocaml/ld.conf", "%s" % get.installDIR(), "")

    pisitools.dodoc("Changes", "INSTALL", "LICENSE", "README", "Upgrading")
