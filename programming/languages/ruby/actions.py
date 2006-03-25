#!/usr/bin/python
# -*- coding: utf-8 -*- 
#
# Copyright 2005 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.
#
# S.Çağlar Onur <caglar@pardus.org.tr>

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

def setup():
    shelltools.export("CFLAGS", get.CFLAGS().replace("-fomit-frame-pointer", ""))
    shelltools.export("CXXFLAGS", get.CXXFLAGS().replace("-fomit-frame-pointer", ""))
    autotools.configure("--enable-shared --enable-pthread")

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())
    pisitools.dodoc("COPYING*", "ChangeLog", "MANIFEST", "README*", "ToDo")
