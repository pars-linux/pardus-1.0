#!/usr/bin/python
# -*- coding: utf-8 -*- 
#
# Copyright 2005 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.
#
# Onur Küçük <onur@pardus.org.tr>

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

ZLIBSRC="libs/zlib-1.2.3"
LPNGSRC="libs/libpng-1.2.8"
JPEGSRC="libs/jpeg-6b"
FT2SRC="libs/freetype-2.1.9"


def setup():
    shelltools.echo("config.h", "#undef CONFIG_SILENT_KD_GRAPHICS")
    shelltools.echo("config.h", "#define CONFIG_PNG 1")
    shelltools.echo("config.h", "#define CONFIG_TTF 1")
    shelltools.echo("config.h", "#define CONFIG_TTF_KERNEL 1")
    
    pisitools.dosed("Makefile", "^CFLAGS[ \t]*=.*", "CFLAGS = %s" % get.CFLAGS())
    # There is no -fno-stack-protector on our gcc 3.4.4 :P
    pisitools.dosed("Makefile", "-fno-stack-protector")

def build():
    shelltools.export("ZLIBSRC", ZLIBSRC)
    shelltools.export("LPNGSRC", LPNGSRC)
    shelltools.export("JPEGSRC", JPEGSRC)
    shelltools.export("FT2SRC", FT2SRC)

    autotools.make("-j1 LIB=lib")

def install():
    shelltools.export("ZLIBSRC", ZLIBSRC)
    shelltools.export("LPNGSRC", LPNGSRC)
    shelltools.export("JPEGSRC", JPEGSRC)
    shelltools.export("FT2SRC", FT2SRC)

    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    pisitools.dodoc("docs/*", "README", "AUTHORS")

    pisitools.dodir("/lib/splash/tmp")
    pisitools.dodir("/lib/splash/cache")
    pisitools.dodir("/lib/splash/bin")
    pisitools.dosym("/lib/splash/bin/fbres", "/sbin/fbres")
