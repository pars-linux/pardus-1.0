#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright © 2005  TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.
#
# Ahmet AYGÜN <ahmet@zion.gen.tr>

from pisi.actionsapi import autotools
from pisi.actionsapi import get
from pisi.actionsapi import pisitools

def setup():
    pisitools.dosed("Makefile", "splint", "#splint")
    pisitools.dosed("Makefile", "-Wall", "-Wall %s -lm" % get.CFLAGS())

def build():
    autotools.make()

def install():
    pisitools.dobin("fbgrab")
    pisitools.newman("fbgrab.1.man", "fbgrab.1")
