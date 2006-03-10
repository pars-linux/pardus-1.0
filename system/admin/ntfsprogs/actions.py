#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright © 2005  TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.
#
# Fatih Aşıcı <fasici@linux-sevenler.org>

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools

def setup():
    pisitools.dosed("configure", "-ggdb3", "")
    autotools.configure("--disable-gnome-vfs --disable-fuse-module")

def build():
    autotools.make()

def install():
    autotools.install()
    pisitools.dodoc("ChangeLog", "AUTHORS", "CREDITS", "NEWS", "README*", "TODO.*", \
                "doc/attribute_definitions", "doc/*.txt", "doc/tunable_settings")
