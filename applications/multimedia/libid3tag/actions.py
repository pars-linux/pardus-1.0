#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2005 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.
#
# Timu EREN <selamtux@gmail.com>

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools

def setup():
    autotools.configure("--with-gnu-ld \
                         --disable-debugging")

def build():
    autotools.make()

def install():
    autotools.install()
    pisitools.dodoc("CHANGES", "COPYRIGHT", "CREDITS", "README", "TODO", "VERSION")
