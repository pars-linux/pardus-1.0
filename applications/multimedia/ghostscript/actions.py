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

WorkDir = "espgs-7.07.1"

def setup():
    pisitools.dosed("Makefile.in", "\$\(gsdatadir\)/lib", "/usr/share/ghostscript/7.07/lib")
    pisitools.dosed("Makefile.in", "$(gsdir)/fonts", "/usr/share/fonts/default/ghostscript/")

    # fix dynamic build
    shelltools.echo("src/png_.h", "#include \"png.h\"")

    autotools.autoconf()
    autotools.configure("--with-ijs \
                        --without-gimp-print \
                        --without-omni \
                        --with-x \
                        --enable-cups \
                        --with-fontconfig \
                        --with-drivers=ALL,gdi \
                        --with-fontpath=/usr/share/fonts:/usr/share/fonts/TTF")

def build():
    autotools.make("-j1")
    autotools.make("so -j1")
    
    shelltools.cd("ijs")
    autotools.configure()
    autotools.make("-j1")

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())
    autotools.rawInstall("DESTDIR=%s" % get.installDIR(), "soinstall")

    pisitools.removeDir("/usr/share/ghostscript/7.07/doc")
    
    pisitools.dodoc("doc/README", "doc/COPYING", "doc/COPYING.LGPL")
    pisitools.dohtml("doc/")

    # Install ijs
    shelltools.cd("ijs")
    pisitools.dodir("/usr/bin")
    pisitools.dodir("/usr/include")
    pisitools.dodir("/usr/lib")
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    # collision with gcc
    pisitools.remove("/usr/share/man/de/man1/ansi2knr.1")
    pisitools.remove("/usr/share/man/man1/ansi2knr.1")
