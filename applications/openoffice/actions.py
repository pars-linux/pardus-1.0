#!/usr/bin/python
# -*- coding: utf-8 -*- 
#
# Copyright 2005 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.
#
# İsmail Dönmez <ismail@pardus.org.tr>

from pisi.actionsapi import pisitools
from pisi.actionsapi import autotools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

WorkDir="ooo-build-2.0.1"

def setup():
    shelltools.system("./autogen.sh \
                       --prefix=/opt/OpenOffice.org \
                       --sysconfdir=/etc \
                       --with-lang=tr \
                       --disable-post-install-scripts \
                       --with-installed-ooo-dirname=ooo-2.0 \
                       --enable-hunspell \
                       --disable-gtk \
                       --with-jdk-home=/opt/blackdown-jdk/ \
                       --disable-cairo \
                       --disable-mono \
                       --disable-access \
                       --with-distro=Pardus")

    shelltools.system("./download")
    
def build():
    shelltools.export("CFLAGS", "-02 -fno-strict-aliasing")
    shelltools.export("LC_ALL", "C")
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    # We have our own desktop files
    pisitools.remove("/usr/share/applications/*")
    
    # Zemberek
    shelltools.system("%s/opt/OpenOffice.org/lib/ooo-2.0/program/unopkg add --shared -v src/zemberek.zip" % get.installDIR())

    # Links
    apps = ["oobase", "oodraw", "oomath", "ooimpress", "oocalc", "oowriter"]
    for app in apps:
        pisitools.dosym("/opt/OpenOffice.org/bin/%s2.0" % app, "/usr/bin/%s" % app)

    # Icon symlinks
    pisitools.dosym("/usr/share/pixmaps/ooo-impress2.0.png","/usr/share/pixmaps/presentation.png")
    pisitools.dosym("/usr/share/pixmaps/ooo-writer2.0.png","/usr/share/pixmaps/wordprocessing.png")
    pisitools.dosym("/usr/share/pixmaps/ooo-calc2.0.png","/usr/share/pixmaps/spreadsheet.png")
    pisitools.dosym("/usr/share/pixmaps/ooo-base2.0.png","/usr/share/pixmaps/database.png")
    pisitools.dosym("/usr/share/pixmaps/ooo-draw2.0.png","/usr/share/pixmaps/drawing.png")
    pisitools.dosym("/usr/share/pixmaps/ooo-math2.0.png","/usr/share/pixmaps/formula.png")
