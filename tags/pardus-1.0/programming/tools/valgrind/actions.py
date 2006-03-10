#!/usr/bin/python
# -*- coding: utf-8 -*- 
#
# Copyright 2005 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.
#
# S.Çağlar Onur <caglar@uludag.org.tr>

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

def setup():
    pisitools.dosed("configure", "CFLAGS=\"-Wno-long-long\"", "CFLAGS=\"%s -Wno-long-long\"" % get.CFLAGS())
    
    autotools.configure("--with-x")   

def build():
    autotools.make()

def install():
    autotools.install("docdir=\"%s/usr/share/doc/${PF}/html\"" % get.installDIR())
    pisitools.dodoc("ACKNOWLEDGEMENTS", "AUTHORS", "FAQ.txt", "NEWS", "README*", "TODO")
