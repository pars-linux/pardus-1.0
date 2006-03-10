#!/usr/bin/python
# -*- coding: utf-8 -*- 
#
# Copyright 2005 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.
#
# Onur Küçük <onur@uludag.org.tr>

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

WorkDir = "mpg123"

def setup():
    pisitools.dosed("0.59s-mh4", "0.59s")

def build():
    autotools.make("clean linux-generic CFLAGS=\"%s\"" % get.CFLAGS())

def install():
    pisitools.insinto("/usr/bin", "mpg123")
    pisitools.doman("mpg123.1")
    pisitools.dodoc("BENCHMARKING", "BUGS", "CHANGES", "COPYING", "JUKEBOX", "README*", "TODO")

