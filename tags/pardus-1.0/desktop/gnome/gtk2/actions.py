#!/usr/bin/python
# -*- coding: utf-8 -*- 
#
# Copyright 2005 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.
#
# Bahadır Kandemir <bahadir@pardus.org.tr>

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

WorkDir = "gtk+-2.8.7"

def setup():
    autotools.autoconf()
    autotools.automake()

    autotools.configure("--disable-gtk-doc \
                         --with-jpeg \
                         --with-libjpeg \
                         --with-libtiff \
                         --with-png \
                         --with-gdktarget=x11 \
                         --with-xinput")

def build():
    autotools.make("-j1")

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())
    pisitools.dodoc("AUTHORS", "README*", "HACKING", "TODO", "ChangeLog*", "NEWS*")
