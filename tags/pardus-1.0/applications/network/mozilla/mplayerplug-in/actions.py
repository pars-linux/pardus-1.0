#!/usr/bin/python
# -*- coding: utf-8 -*- 
#
# Copyright 2005 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.
#
# Name <email@address>

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

WorkDir = "mplayerplug-in"

def setup():
    autotools.configure("--enable-gtk2")

def build():
    autotools.make()

def install():
    pisitools.insinto("/usr/lib/nsbrowser/plugins/", "*.so")
    pisitools.insinto("/usr/lib/nsbrowser/plugins/", "*.xpt")
    
    pisitools.insinto("/etc", "mplayerplug-in.conf")
    pisitools.insinto("/etc", "mplayerplug-in.types")
