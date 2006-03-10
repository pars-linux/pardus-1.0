#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright © 2005  TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.
#
# S.Çağlar Onur <caglar@uludag.org.tr>

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

def setup():
    # Don't build or install locate because it conflicts with slocate,
    # which is a secure version of locate.
    pisitools.dosed("Makefile.in", "SUBDIRS = gnulib lib intl find xargs locate doc po", "SUBDIRS = gnulib lib intl find xargs doc po")
    
    autotools.configure("--enable-nls")

def build():
    shelltools.export("CPPFLAGS", get.CXXFLAGS())
    autotools.make("libexecdir=/usr/lib/find")

def install():
    autotools.install("libexecdir=%s/usr/lib/find/usr/lib/find" % get.installDIR())
    pisitools.dodoc("ChangeLog", "NEWS", "TODO", "README")
