#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright © 2005  TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.
#
# Fatih Aşıcı <fasici@linux-sevenler.org>

from pisi.actionsapi import autotools
from pisi.actionsapi import shelltools
from pisi.actionsapi import pisitools

def setup():
    autotools.make("-f Makefile.dist")
    autotools.configure("--enable-labels")
    shelltools.echo("data/qtparted.desktop", "X-KDE-SubstituteUID=true")
    shelltools.echo("data/qtparted.desktop", "X-KDE-Username=root")

def build():
    autotools.make()

def install():
    autotools.install()
    pisitools.domove("/usr/share/applnk/System/qtparted.desktop", "/usr/share/applications/")
    pisitools.removeDir("/usr/share/applnk")
    pisitools.dodoc("doc/TODO.txt", "doc/BUGS", "doc/DEVELOPER-FAQ", "doc/README*")
