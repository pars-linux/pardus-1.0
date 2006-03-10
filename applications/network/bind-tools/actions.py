#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright (C) 2005, TUBITAK/UEKAE
#
# This program is free software; you can redistribute it and/or modify it under
# the terms of the GNU General Public License as published by the Free
# Software Foundation; either version 2 of the License, or (at your option)
# any later version.
#
# Timu EREN <selamtux@gmail.com>.
#

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools

WorkDir = "bind-9.3.1"

def setup():
    autotools.configure("--enable-ipv6 \
                         --enable-libbind")

def build():
    shelltools.export("MAKEOPTS","-j1")
    #make for all becouse required libbind
    autotools.make()

def install():
    # binaries
    pisitools.dobin("bin/dig/dig")
    pisitools.dobin("bin/dig/host") 
    pisitools.dobin("bin/dig/nslookup")
    # man and doc files
    pisitools.doman("bin/dig/dig.1", "bin/dig/host.1", "bin/dig/nslookup.8")
    pisitools.dodoc("CHANGES", "FAQ", "README")
