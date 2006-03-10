#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright © 2005  TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.
#
# Furkan Duman <coderlord@gmail.com>

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

def setup():
    autotools.configure("--enable-user-local=no --with-ssl --with-plugins=/usr/lib/ethereal/plugins")

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())
    pisitools.dodoc("AUTHORS", "ChangeLog", "FAQ", "COPYING", "NEWS", "README*")
    pisitools.insinto("/usr/share/icons/hicolor/48x48/apps", "image/hi48-app-ethereal.png", "ethereal.png")
    pisitools.insinto("/usr/share/applications/", "ethereal.desktop")
