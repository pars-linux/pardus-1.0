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
from pisi.actionsapi import get

def setup():
    autotools.configure("--enable-mmx --enable-sse")

def build():
    autotools.make()

def install():
    pisitools.dodir("/usr")
    pisitools.dodir("/usr/lib")

    autotools.install()
    
    pisitools.dobin("libfame-config")

    pisitools.insinto("/usr/share/aclocal", "libfame.m4")

    pisitools.dodoc("CHANGES", "README")
    pisitools.doman("doc/*.3")
