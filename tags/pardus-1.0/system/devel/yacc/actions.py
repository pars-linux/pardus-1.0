#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright © 2005  TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.
#
# S.Çağlar Onur <caglar@pardus.org.tr>

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

def setup():
    pisitools.dosed("Makefile", " -O ", " $(CFLAGS) ")

def build():
    autotools.make("clean")
    autotools.make("-j1 CC=\"%s\" CFLAGS=\"%s\"" % (get.CC(), get.CFLAGS()))

def install():
    pisitools.dobin("yacc")
    pisitools.doman("yacc.1")
    pisitools.dodoc("00README*", "ACKNOWLEDGEMENTS", "NEW_FEATURES", "NO_WARRANTY", "NOTES", "README*")
