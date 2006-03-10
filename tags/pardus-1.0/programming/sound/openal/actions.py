# Copyright © 2005  TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file `http://www.gnu.org/copyleft/gpl.txt'.
#
#!/usr/bin/python
# -*- coding: utf-8 -*- 
#
# A. Murat Eren <meren@uludag.org.tr>

from pisi.actionsapi import shelltools
from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

def setup():
    shelltools.cd("linux")
    shelltools.export("WANT_AUTOCONF", "2.5")

    autotools.autoheader()
    autotools.autoconf()
    autotools.configure("--enable-esd \
                         --enable-sdl \
                         --enable-alsa \
                         --enable-arts \
                         --disable-smpeg \
                         --enable-vorbis \
                         --enable-paranoid-locks \
                         --libdir=/usr/lib \
                         --enable-capture \
                         --enable-optimize")

def build():
    shelltools.cd("linux")

    autotools.make("all")

def install():
    shelltools.cd("linux")

    autotools.rawInstall("DESTDIR=%s" % get.installDIR()) 

    pisitools.dodoc("CREDITS", "ChangeLog", "INSTALL",\
                    "NOTES", "PLATFORM", "TODO")

    shelltools.cd("..")

    pisitools.dodoc("CHANGES", "COPYING", "CREDITS")
    pisitools.dohtml("docs/*.html")
