#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright © 2005  TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.
#
# Ahmet AYGÜN <ahmet@zion.gen.tr>

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools

def setup():
    autotools.configure("--with-xml2 \
                        --with-ssl \
                        --with-zlib \
                        --enable-shared")

def build():
    autotools.make()

def install():
    autotools.install()
    pisitools.dodoc("THANKS", "TODO", "ChangeLog", "AUTHORS", "BUGS", "NEWS", "README", "doc/*")
