#!/usr/bin/python
# -*- coding: utf-8 -*- 
#
# Copyright 2005 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.
#
# Gürer Özen <gurer@pardus.org.tr>

from pisi.actionsapi import autotools
from pisi.actionsapi import libtools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

def setup():
    autotools.autoconf()
    libtools.libtoolize("--copy --force")
    autotools.configure("--without-gnome-print \
                        --without-gnome-vfs \
                        --with-python")

def build():
    autotools.make()

def install():
    autotools.install()
    pisitools.dodoc("AUTHORS", "TRANSLATORS", "COPYING", "COPYING.LIB", "ChangeLog", "HACKING", "NEWS", "README")
